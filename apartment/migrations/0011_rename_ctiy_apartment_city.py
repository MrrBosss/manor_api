# Generated by Django 4.0.10 on 2024-08-01 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0010_remove_apartment_company_logo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apartment',
            old_name='ctiy',
            new_name='city',
        ),
    ]
