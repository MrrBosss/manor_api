# Generated by Django 4.0.10 on 2024-08-20 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0016_remove_apartment_convandcon_delete_convandcon'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apartment',
            options={'verbose_name': 'Turar joy', 'verbose_name_plural': 'Turar joylar'},
        ),
        migrations.AlterModelOptions(
            name='apartmentshots',
            options={'verbose_name': 'Turar joy rasmi', 'verbose_name_plural': 'Turar joy rasmlari'},
        ),
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': 'Brend', 'verbose_name_plural': 'Brendlar'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Kategoriya', 'verbose_name_plural': 'Kategoriyalar'},
        ),
        migrations.AlterModelOptions(
            name='characteristic',
            options={'verbose_name': 'Xarakteristika', 'verbose_name_plural': 'Xarakteristikalar'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Shahar', 'verbose_name_plural': 'Shaharlar'},
        ),
        migrations.AlterModelOptions(
            name='district',
            options={'verbose_name': 'Tuman', 'verbose_name_plural': 'Tumanlar'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Zakaz', 'verbose_name_plural': 'Zakazlar'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Proyekt', 'verbose_name_plural': 'Proyektlar'},
        ),
    ]
