# Generated by Django 5.0 on 2023-12-22 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='instrument_type',
            field=models.CharField(choices=[('Guitar', 'Guitar'), ('Piano', 'Piano'), ('Violin', 'Violin'), ('Cello', 'Cello'), ('Brass instrument', 'Brass instrument')], max_length=50),
        ),
    ]
