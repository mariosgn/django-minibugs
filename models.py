from django.conf import settings
from django.db import models

STATUSES = [('N', 'New'),
            ('W', 'Working'),
            ('F', 'Fixed'),
            ('V', 'Verified'),
            ('T', 'Won\'t Fix'),
            ('B', 'Not a Bug'),
            ('C', 'Closed'),
            ]

TYPES = [('D', 'Defect'),
        ('E', 'Enhancement')]


PRIORITIES = [('L', 'Low'),
              ('M', 'Medium'),
              ('H', 'High')]


class Ticket(models.Model):
    title = models.CharField(max_length=250)
    created_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
    current = models.ForeignKey('TicketUpdate', null=True, blank=True, related_name='current')

    class Meta:
        ordering = ['created_time']

    def __unicode__(self):
        return self.title


class TicketUpdate(models.Model):
    ticket = models.ForeignKey(Ticket)
    description = models.TextField()
    attachment = models.FileField(upload_to='minibugs', blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUSES, default='N')
    type = models.CharField(max_length=1, choices=TYPES, default='N')
    priority = models.CharField(max_length=1, choices=PRIORITIES, default='D')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+', blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_time']

    def __unicode__(self):
        return '%s: %s' % (self.ticket.title, self.ticket.id)