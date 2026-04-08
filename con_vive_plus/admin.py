from django.contrib import admin
from .models import House, ContactMessage

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    search_fields = ('name', 'city')
    ordering = ('name',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
      list_display = ('name', 'email', 'created_at')
      search_fields = ('name','email')
      ordering = ('-created_at',)





