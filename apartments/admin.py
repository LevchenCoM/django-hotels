from django.contrib import admin
from django.conf import settings
from .models import *
# Register your models here.


class ApartmentImageInline(admin.TabularInline):
    model = ApartmentImage
    extra = 0

class ApartmentPropertyInline(admin.TabularInline):
    model = ApartmentProperty
    extra = 0

@admin.register(Apartment) #регистрация в админке
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ['is_active', 'name', 'price', 'special_offer', 'special_price', 'created', 'updated']
    list_display_links = ['name']
    inlines = [ApartmentImageInline, ApartmentPropertyInline]

    class Meta:
        model = Apartment
    class Media:
        js = (settings.TINYMCE_JS_URL,)

@admin.register(ApartmentImage)
class ApartmentImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ApartmentImage._meta.fields]

    class Meta:
        model = ApartmentImage

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Property._meta.fields]

    class Meta:
        model = Property

@admin.register(ApartmentProperty)
class ApartmentPropertyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ApartmentProperty._meta.fields]

    class Meta:
        model = ApartmentProperty

# @admin.register(ApartmentDates)
# class ApartmentDatesAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in ApartmentDates._meta.fields]
#
#     class Meta:
#         model = ApartmentDates
