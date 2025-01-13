from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'authors_list', 'count')  
    
    search_fields = ('name', 'authors__name')  
    
    list_filter = ('authors',)  
    
    fieldsets = (
        ('Book Information', {
            'fields': ('name', 'description', 'count', 'authors')
        }),
    )

    def authors_list(self, obj):
        return ', '.join([author.name for author in obj.authors.all()])
    authors_list.short_description = 'Authors'  
