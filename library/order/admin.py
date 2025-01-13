from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'user', 'created_at', 'get_status')  
    
    list_filter = ('created_at',)  
    
    search_fields = ('book__title', 'user__username')
    
    def get_status(self, obj):
        """
        A custom method to display the status of an order.
        If 'end_at' is None, the status is 'Pending', otherwise it's 'Closed'.
        """
        return 'Closed' if obj.end_at else 'Pending'
    
    get_status.admin_order_field = 'end_at'  
    get_status.short_description = 'Status'  
