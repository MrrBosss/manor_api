# Generated by Django 4.0.10 on 2024-08-06 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0020_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apartment.location'),
        ),
    ]
