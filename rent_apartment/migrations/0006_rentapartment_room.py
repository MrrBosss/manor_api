# Generated by Django 4.0.10 on 2024-09-03 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_apartment', '0005_alter_characteristic_icon_alter_characteristic_label_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentapartment',
            name='room',
            field=models.IntegerField(blank=True, null=True, verbose_name='Xonalar soni'),
        ),
    ]
