# Generated by Django 4.0.4 on 2022-05-03 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='banner',
            field=models.ImageField(blank=True, upload_to='blog/banner/'),
        ),
    ]