# Generated by Django 4.1.5 on 2023-01-18 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='photo',
            field=models.ImageField(upload_to='media/photos/%Y/%m/%d'),
        ),
    ]
