# Generated by Django 4.2.4 on 2023-08-09 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0002_pizza_image_name_with_file_extension'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='image_name_with_file_extension',
        ),
        migrations.AddField(
            model_name='pizza',
            name='image',
            field=models.ImageField(default='default', upload_to='pizzas/static/media/'),
            preserve_default=False,
        ),
    ]
