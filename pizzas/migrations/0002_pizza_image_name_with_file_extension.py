# Generated by Django 4.2.4 on 2023-08-09 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='image_name_with_file_extension',
            field=models.CharField(default='default_image.png', max_length=100),
        ),
    ]
