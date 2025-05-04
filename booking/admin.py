from django.contrib import admin
from .models import Ticket, Flight, Train, Bus

# Register the Ticket model with its custom admin configuration
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('passenger_name', 'source', 'destination', 'journey_date')
    list_filter = ('is_confirmed', 'journey_date')
    search_fields = ('passenger_name', 'source', 'destination')

# Register other models without custom admin
admin.site.register(Flight)
admin.site.register(Train)
admin.site.register(Bus)
