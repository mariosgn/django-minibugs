from django.forms import Form, ModelForm, CharField, ChoiceField
from .models import TicketUpdate, PRIORITIES, TYPES, STATUSES

class TicketFormUpdate(ModelForm):

    def __init__(self, *args, **kwargs):
        super(TicketFormUpdate, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ['description', 'priority', 'type', 'status', 'attachment']

    class Meta:
        model = TicketUpdate
        fields = ['description', 'priority', 'type', 'status', 'attachment']

class TicketFormCreate(ModelForm):
    title = CharField(required=True)

    def __init__(self, *args, **kwargs):
        super(TicketFormCreate, self).__init__(*args, **kwargs)
        self.fields.keyOrder = [
        'title',
        'description',
        'priority',
        'type',
        'attachment']

    class Meta:
        model = TicketUpdate
        fields = ['title', 'description', 'priority', 'type','attachment']


class TicketFormFilter(Form):
    priority = ChoiceField(choices=[('','---------')]+PRIORITIES, required=False)
    status = ChoiceField(choices=[('','---------')]+STATUSES, required=False)
    type = ChoiceField(choices=[('','---------')]+TYPES, required=False)
    description = CharField(required=False)
    title = CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(TicketFormFilter, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ['priority', 'type','status','title', 'description','author','attachment']

    class Meta:
        model = TicketUpdate
        fields = ['priority', 'type','status','title', 'description','author','attachment']


