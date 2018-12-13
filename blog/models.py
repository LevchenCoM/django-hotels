from django.db import models
from tinymce import models as tinymce_models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=32, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Post(models.Model):
    subject = models.CharField(max_length=128, blank=False, null=False)
    short_description = models.TextField(max_length=68, blank=False, null=False)
    content = tinymce_models.HTMLField('Content')
    slug = models.SlugField(max_length=128, unique=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "{}".format(self.subject)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
