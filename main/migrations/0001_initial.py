# Generated by Django 5.0.7 on 2024-07-25 15:39

import django.db.models.deletion
import parler.fields
import parler.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MotorcycleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255, verbose_name='موديل')),
                ('rental_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='سعر الإيجار')),
                ('image', models.ImageField(upload_to='motorcycle_images/', verbose_name='صورة')),
                ('active', models.BooleanField(default=True, verbose_name='نشط')),
            ],
            options={
                'verbose_name': 'موديل الدراجة النارية',
                'verbose_name_plural': 'موديلات الدراجات النارية',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Motorcycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chassis_number', models.CharField(max_length=255, unique=True, verbose_name='رقم الهيكل')),
                ('rented', models.BooleanField(default=False)),
                ('motorcycle_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Motorcycles', to='main.motorcyclemodel', verbose_name='موديل الدراجة النارية')),
            ],
            options={
                'verbose_name': 'دراجة نارية',
                'verbose_name_plural': 'دراجات نارية',
            },
        ),
        migrations.CreateModel(
            name='MotorcycleModelTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('country_of_origin', models.CharField(max_length=128, verbose_name='بلد المنشأ')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='main.motorcyclemodel')),
            ],
            options={
                'verbose_name': 'موديل الدراجة النارية Translation',
                'db_table': 'main_motorcyclemodel_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
