# Generated by Django 4.0.4 on 2022-05-02 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='firstname',
            field=models.CharField(default='Mide', max_length=104),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='lastname',
            field=models.CharField(default='Dickson', max_length=104),
            preserve_default=False,
        ),
    ]
