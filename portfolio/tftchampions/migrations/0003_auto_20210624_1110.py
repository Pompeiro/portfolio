# Generated by Django 3.1.12 on 2021-06-24 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tftchampions', '0002_auto_20210624_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='champion',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Name of champion'),
        ),
    ]