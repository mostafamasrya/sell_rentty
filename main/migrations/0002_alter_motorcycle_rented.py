# Generated by Django 5.0.7 on 2024-07-25 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motorcycle',
            name='rented',
            field=models.BooleanField(default=False, verbose_name='تم التأجير'),
        ),
    ]
