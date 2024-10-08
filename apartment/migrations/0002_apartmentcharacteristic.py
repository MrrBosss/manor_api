# Generated by Django 4.0.10 on 2024-09-03 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rent_apartment', '0003_remove_apartmentcharacteristic_apartment'),
        ('apartment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApartmentCharacteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=255, null=True, verbose_name='qiymat')),
                ('apartment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='characteristics', to='apartment.apartment')),
                ('characteristic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rent_apartment.characteristic')),
            ],
            options={
                'verbose_name': 'Xarakteristika',
                'verbose_name_plural': 'Xarakteristikalar',
            },
        ),
    ]
