# Generated by Django 3.1.12 on 2021-06-29 09:42

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('image', models.ImageField(upload_to='templatematching')),
                ('needle', models.CharField(choices=[('acceptGameButton', 'Accept game button'), ('afterLogINButton', 'After login button(play button)'), ('confirmationButton', 'Confirmation button'), ('findMatchButton', 'Find match button'), ('inQueueFindingMatch', 'In queue finding match text'), ('playGameButton', 'Play game button')], max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]