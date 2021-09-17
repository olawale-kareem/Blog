from django.contrib import admin
from .models import Address,Books,Author,Country

class BooksAdmin(admin.ModelAdmin): #This class is added to fine tune the Books model display
    # readonly_fields = ('slug',)                 #if you wanna make the field read only
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'rating')
    list_display =('title', 'author', 'rating')
admin.site.register(Books,BooksAdmin) # registers the Books model and the BoksAdmin



class AuthorAdmin(admin.ModelAdmin): 
    list_filter = ('first_name', )
    list_display =('first_name', 'last_name')
admin.site.register(Author, AuthorAdmin)


class AddressAdmin(admin.ModelAdmin): 
    list_filter = ('city',)
    list_display =('street','postal_code', 'city')
admin.site.register(Address, AddressAdmin)


class CountryAdmin(admin.ModelAdmin): 
    list_filter = ('name',)
    list_display =('name','code')
admin.site.register(Country, CountryAdmin)
