# Generated by Django 4.0.10 on 2024-08-23 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_apartment', '0018_condition_name_en_condition_name_ru_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Sharoit'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='name_en',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Sharoit'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='name_ru',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Sharoit'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='name_uz',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Sharoit'),
        ),
        migrations.AlterField(
            model_name='convenience',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Qulaylik'),
        ),
        migrations.AlterField(
            model_name='convenience',
            name='name_en',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Qulaylik'),
        ),
        migrations.AlterField(
            model_name='convenience',
            name='name_ru',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Qulaylik'),
        ),
        migrations.AlterField(
            model_name='convenience',
            name='name_uz',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Qulaylik'),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Manzil nomi'),
        ),
        migrations.AlterField(
            model_name='rentapartment',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name="Ta'rif"),
        ),
        migrations.AlterField(
            model_name='rentapartment',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name="Ta'rif"),
        ),
        migrations.AlterField(
            model_name='rentapartment',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name="Ta'rif"),
        ),
        migrations.AlterField(
            model_name='rentapartment',
            name='description_uz',
            field=models.TextField(blank=True, null=True, verbose_name="Ta'rif"),
        ),
        migrations.AlterField(
            model_name='rentapartmentorder',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Izoh'),
        ),
        migrations.AlterField(
            model_name='rentapartmentorder',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ism'),
        ),
        migrations.AlterField(
            model_name='rentapartmentorder',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefon raqam'),
        ),
    ]
