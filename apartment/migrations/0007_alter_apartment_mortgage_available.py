# Generated by Django 4.0.10 on 2024-10-06 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0006_brand_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='mortgage_available',
            field=models.BooleanField(default=False, verbose_name='Ipoteka'),
        ),
    ]
