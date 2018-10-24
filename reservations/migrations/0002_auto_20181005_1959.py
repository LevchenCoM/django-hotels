# Generated by Django 2.1 on 2018-10-05 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='check_in_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='check_out_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='apartmentinreservation',
            name='apartment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apartments.Apartment'),
        ),
        migrations.AlterField(
            model_name='apartmentinreservation',
            name='reservation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservations.Reservation'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='customer_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='customer_name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='customer_phone',
            field=models.CharField(blank=True, max_length=48, null=True),
        ),
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
    ]
