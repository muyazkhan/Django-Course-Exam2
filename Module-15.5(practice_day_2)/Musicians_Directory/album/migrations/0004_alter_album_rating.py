# Generated by Django 5.0 on 2023-12-22 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0003_alter_album_musician'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
    ]
