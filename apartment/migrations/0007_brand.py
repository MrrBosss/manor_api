# Generated by Django 4.0.10 on 2024-08-01 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0006_apartment_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('brand_image', models.ImageField(blank=True, upload_to='brand-images')),
            ],
        ),
    ]
