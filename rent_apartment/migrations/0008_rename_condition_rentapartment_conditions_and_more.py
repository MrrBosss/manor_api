# Generated by Django 4.0.10 on 2024-09-05 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent_apartment', '0007_alter_location_apartment_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rentapartment',
            old_name='condition',
            new_name='conditions',
        ),
        migrations.RenameField(
            model_name='rentapartment',
            old_name='convenience',
            new_name='conveniences',
        ),
    ]
