# Generated by Django 5.0 on 2023-12-26 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_car_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(max_length=500, null=True, unique=True),
        ),
    ]