from django.contrib import admin
from .models import NavigationMenuLinks
# Register your models here.

@admin.register(NavigationMenuLinks) #регистрация в админке
class NavigationMenuLinksAdmin(admin.ModelAdmin):
    list_display = [field.name for field in NavigationMenuLinks._meta.fields]

    class Meta:
        model = NavigationMenuLinks
