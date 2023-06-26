# Generated by Django 4.2.2 on 2023-06-26 10:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fut_pole', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='owner',
            options={'verbose_name': 'Владелец', 'verbose_name_plural': 'Владельцы'},
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='datetime',
            new_name='selected_date',
        ),
        migrations.AddField(
            model_name='booking',
            name='selected_end_time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Конечное время'),
        ),
        migrations.AddField(
            model_name='booking',
            name='selected_start_time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Начальное время'),
        ),
    ]