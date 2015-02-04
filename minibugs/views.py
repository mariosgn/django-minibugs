from django.contrib.auth import get_user
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormMixin
from django.views.generic.edit import BaseFormView
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required

from .models import Ticket, TicketUpdate
from .forms import TicketFormCreate, TicketFormUpdate, TicketFormFilter

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

class MinibugsHome(LoginRequiredMixin, ListView):
    template_name = "minibugs/list.html"
    model = Ticket
    fields = ['id']
    paginate_by = 10
    success_url = reverse_lazy('minibugs_home')
    filtering = False;

    def get_form(self, **kwargs):
        if 'csrfmiddlewaretoken' in self.request.GET and self.request.GET['csrfmiddlewaretoken'] is not None:
            form = TicketFormFilter( self.request.GET )
            form.is_valid()
        else:
            form = TicketFormFilter()
        return form

    def get_context_data(self, **kwargs):
        ctx = super(MinibugsHome, self).get_context_data(**kwargs)
        ctx["form"] = self.get_form()
        ctx["filtering"] = self.filtering
        return ctx

    def get_queryset(self):
        qs = super(MinibugsHome, self).get_queryset()
        form = self.get_form()
        if form.is_valid():

            #for field in form.cleaned_data:
            #    if len(field) > 0:
            #        qs = qs.filter(**{field+'__contains': form.cleaned_data[field]})
            #        self.filtering = True

            if len(form.cleaned_data["title"]) > 0:
                qs = qs.filter(title__icontains=form.cleaned_data["title"])
                self.filtering = True

            if len(form.cleaned_data["priority"]) > 0:
                qs = qs.filter(current__priority=form.cleaned_data["priority"])
                self.filtering = True

            if len(form.cleaned_data["status"]) > 0:
                qs = qs.filter(current__status=form.cleaned_data["status"])
                self.filtering = True

            if len(form.cleaned_data["type"]) > 0:
                qs = qs.filter(current__type=form.cleaned_data["type"])
                self.filtering = True

            if len(form.cleaned_data["description"]) > 0:
                qs = qs.filter(current__description__icontains=form.cleaned_data["description"])
                self.filtering = True

        return qs.order_by("-created_time")


class MinibugsDetails(LoginRequiredMixin, ListView):
    template_name = "minibugs/details.html"
    model = TicketUpdate
    fields = ['id']

    def get_context_data(self, **kwargs):
        ctx = super(MinibugsDetails, self).get_context_data(**kwargs)
        ctx.update({"ticket":Ticket.objects.get(id=self.kwargs["pk"])})
        return ctx

    def get_queryset(self):
        tid = self.kwargs["pk"]
        return super(MinibugsDetails, self).get_queryset().filter(ticket_id=tid)


class MinibugsCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "minibugs/edit.html"
    model = TicketUpdate
    form_class = TicketFormCreate
    success_url = reverse_lazy('minibugs_home')
    success_message = "Ticket %d created"

    def get_success_message(self, cleaned_data):
        return self.success_message % self.object.ticket.id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        t = Ticket.objects.create(created_by=get_user(self.request))
        self.object.ticket = t
        self.object.author = get_user(self.request)

        self.object.save()
        t.title = form.cleaned_data["title"]
        t.current = self.object
        t.save()
        return super(MinibugsCreate, self).form_valid(form)


class MinibugsUpdate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "minibugs/edit.html"
    model = TicketUpdate
    form_class = TicketFormUpdate
    success_message = "Ticket %d updated"

    def get_initial(self):
        initial = model_to_dict( TicketUpdate.objects.filter(ticket_id=self.kwargs["pk"]).first() )
        del initial["attachment"]
        del initial["description"]
        return initial

    def get_context_data(self, **kwargs):
        ctx = super(MinibugsUpdate, self).get_context_data(**kwargs)
        ctx.update({"ticket":Ticket.objects.get(id=self.kwargs["pk"])})
        return ctx

    def get_success_url(self):
        return reverse_lazy('minibugs_details', kwargs = self.kwargs)

    def get_success_message(self, cleaned_data):
        return self.success_message % self.object.ticket.id

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.ticket_id = self.kwargs["pk"]
        self.object.author = get_user(self.request)
        self.object.save()

        ticket = Ticket.objects.get(id=self.kwargs["pk"])
        ticket.current = self.object
        ticket.save()
        return super(MinibugsUpdate, self).form_valid(form)
