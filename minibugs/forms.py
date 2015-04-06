from django.forms import Form, ModelForm, CharField, ChoiceField, MultipleChoiceField
from .models import TicketUpdate, PRIORITIES, TYPES, STATUSES

class TicketFormUpdate(ModelForm):

    class Meta:
        model = TicketUpdate
        fields = ['description', 'priority', 'type', 'status', 'attachment']

class TicketFormCreate(ModelForm):
    title = CharField(required=True)
    viewname = CharField(required=False)

    class Meta:
        model = TicketUpdate
        fields = ['title', 'description', 'viewname', 'priority', 'type','attachment']


class TicketFormFilter(Form):
    priority = MultipleChoiceField(choices=[('','---------')]+PRIORITIES, required=False)
    status = MultipleChoiceField(choices=[('','---------')]+STATUSES, required=False)
    type = MultipleChoiceField(choices=[('','---------')]+TYPES, required=False)
    description = CharField(required=False)
    title = CharField(required=False)
    viewname = CharField(required=False)