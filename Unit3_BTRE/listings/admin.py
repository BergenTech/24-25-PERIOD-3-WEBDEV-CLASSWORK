from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'dollar_price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 20
    def dollar_price(self, obj):
        return f"${obj.price:,}"
    
    dollar_price.short_description = 'price'

# Register your models here.
admin.site.register(Listing, ListingAdmin)