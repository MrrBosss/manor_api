# Generated by Django 4.0.10 on 2024-08-22 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_and_banners', '0003_alter_banner_image_alter_banner_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='alias',
            field=models.URLField(blank=True, null=True, verbose_name='Link'),
        ),
    ]
