from django.contrib import admin
from .models import Ticket, TicketUpdate

class TicketAdmin(admin.ModelAdmin):
    list_display = ('title',)

class TicketUpdateAdmin(admin.ModelAdmin):
    list_display = ('id',  'ticket','description','status','created_time')

admin.site.register(TicketUpdate, TicketUpdateAdmin)
admin.site.register(Ticket, TicketAdmin)

