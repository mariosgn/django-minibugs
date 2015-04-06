from django.utils.encoding import force_text
from django.conf import settings
from django.template.loader import render_to_string

from .models import Ticket, TicketUpdate


import re

_HTML_TYPES = ('text/html', 'application/xhtml+xml')

class MinibugsMiddleware:

    def process_response(self, request, response):
        # Check for responses where the toolbar can't be inserted.
        content_encoding = response.get('Content-Encoding', '')
        content_type = response.get('Content-Type', '').split(';')[0]
        if any((getattr(response, 'streaming', False),
                'gzip' in content_encoding,
                content_type not in _HTML_TYPES)):
            return response

        # Insert the toolbar in the response.
        content = force_text(response.content, encoding=settings.DEFAULT_CHARSET)
        insert_before = "</body>"
        try:                    # Python >= 2.7
            pattern = re.escape(insert_before)
            bits = re.split(pattern, content, flags=re.IGNORECASE)
        except TypeError:       # Python < 2.7
            pattern = '(.+?)(%s|$)' % re.escape(insert_before)
            matches = re.findall(pattern, content, flags=re.DOTALL | re.IGNORECASE)
            bits = [m[0] for m in matches if m[1] == insert_before]
            # When the body ends with a newline, there's two trailing groups.
            bits.append(''.join(m[0] for m in matches if m[1] == ''))
        if len(bits) > 1:
            vn = request.resolver_match.url_name
            ts = Ticket.objects.filter(viewname=vn).all()

            context = { 'view_name': vn, "tickets": ts }
            bits[-2] += render_to_string('minibugs/modalpage.html', context)
            response.content = insert_before.join(bits)
            if response.get('Content-Length', None):
                response['Content-Length'] = len(response.content)
        return response