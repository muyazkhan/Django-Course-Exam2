# Generated by Django 5.0 on 2023-12-22 03:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_alter_album_rating'),
        ('musician', '0002_alter_musician_instrument_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='musician',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album', to='musician.musician'),
        ),
    ]
