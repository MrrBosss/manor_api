# Generated by Django 4.0.10 on 2024-08-20 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0011_remove_apartment_convandcon_apartment_convandcon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='characteristics',
        ),
        migrations.AddField(
            model_name='characteristic',
            name='apartment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apartment.apartment'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='apartment_sold',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apartment.brand'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apartment.category'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apartment.city'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='company_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apartment.district'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='is_finish',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='mortgage_available',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='name_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='name_ru',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='name_uz',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='price',
            field=models.FloatField(blank=True, default=10.0, null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='price_per_m',
            field=models.FloatField(blank=True, default=1.0, null=True),
        ),
        migrations.AlterField(
            model_name='apartmentshots',
            name='apartment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='apartment_shots', to='apartment.apartment'),
        ),
    ]
