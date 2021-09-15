from django.contrib import admin
from .models import Books

class BooksAdmin(admin.ModelAdmin):
    # readonly_fields = ('slug',)                 #if you wanna make the field read only
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'rating')
    list_display =('title', 'author', 'rating')

admin.site.register(Books,BooksAdmin)

