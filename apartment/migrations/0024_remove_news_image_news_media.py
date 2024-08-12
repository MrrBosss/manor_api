# Generated by Django 4.0.10 on 2024-08-06 10:45

import apartment.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0023_alter_news_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='image',
        ),
        migrations.AddField(
            model_name='news',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to='news', validators=[apartment.validators.validate_image_or_video]),
        ),
    ]
