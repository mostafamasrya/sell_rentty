# Generated by Django 5.0.7 on 2024-07-28 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_contactrequest_selected_motorcycle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactrequest',
            name='message',
            field=models.TextField(blank=True, null=True, verbose_name='Message'),
        ),
    ]
