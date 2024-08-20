# Generated by Django 4.0.10 on 2024-08-15 14:22

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0004_remove_location_apartment'),
        ('rent_apartment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentapartment',
            name='location',
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('apartment', models.ForeignKey(null=True, on_delete=django.db.models.expressions.Case, to='apartment.apartment')),
                ('rent_apartment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rent_apartment.rentapartment')),
            ],
        ),
    ]
