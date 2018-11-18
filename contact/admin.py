from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ContactMessage._meta.fields]

    class Meta:
        model = ContactMessage
