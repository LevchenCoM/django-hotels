# Generated by Django 2.1 on 2018-12-13 06:46

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0011_auto_20181213_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='description',
            field=tinymce.models.HTMLField(default='', verbose_name='Content'),
        ),
    ]