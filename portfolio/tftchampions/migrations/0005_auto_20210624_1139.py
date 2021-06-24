# Generated by Django 3.1.12 on 2021-06-24 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tftchampions', '0004_auto_20210624_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='champion',
            name='class_sec',
            field=models.CharField(blank=True, max_length=30, verbose_name='Class secondary of champion'),
        ),
        migrations.AlterField(
            model_name='champion',
            name='origin_sec',
            field=models.CharField(blank=True, max_length=30, verbose_name='Origin secondary of champion'),
        ),
    ]
