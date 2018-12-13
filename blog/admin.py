from django.contrib import admin
from django.conf import settings
from .models import Post
# Register your models here.

@admin.register(Post) #регистрация в админке
class PostAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Post._meta.fields]

    class Meta:
        model = Post
    class Media:
        js = (settings.TINYMCE_JS_URL,)
