# Generated by Django 4.0.10 on 2024-08-01 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0008_city_apartment_is_mortgage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apartment.brand'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='ctiy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apartment.city'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apartment.district'),
        ),
    ]
