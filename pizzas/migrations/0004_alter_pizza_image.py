# Generated by Django 4.2.4 on 2023-08-09 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0003_remove_pizza_image_name_with_file_extension_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
