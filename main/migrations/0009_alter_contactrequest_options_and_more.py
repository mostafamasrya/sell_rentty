# Generated by Django 4.2 on 2024-10-30 15:07

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_contactrequest_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactrequest',
            options={'verbose_name': 'طلب اتصال', 'verbose_name_plural': 'طلبات الاتصال'},
        ),
        migrations.AddField(
            model_name='contactrequest',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='تاريخ الانشاء'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactrequest',
            name='delivery_app_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='اسم تطبيق التوصيل'),
        ),
        migrations.AddField(
            model_name='contactrequest',
            name='manager_id',
            field=models.FileField(blank=True, null=True, upload_to='manager_id/', verbose_name='هوية المدير'),
        ),
        migrations.AddField(
            model_name='contactrequest',
            name='mobile',
            field=models.CharField(max_length=32, null=True, verbose_name='رقم الجوال'),
        ),
        migrations.AddField(
            model_name='contactrequest',
            name='monthly_deposits',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='مبالغ الإيداعات الشهرية من تطبيقات التوصيل'),
        ),
        migrations.AddField(
            model_name='contactrequest',
            name='owner_id',
            field=models.FileField(blank=True, null=True, upload_to='owner_id/', verbose_name='هوية المالك'),
        ),
        migrations.AddField(
            model_name='contactrequest',
            name='representatives_count',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='عدد المناديب'),
        ),
        migrations.AddField(
            model_name='contactrequest',
            name='transport_license',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='ترخيص هيئة النقل'),
        ),
        migrations.AddField(
            model_name='contactrequest',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث'),
        ),
        migrations.AddField(
            model_name='contactrequest',
            name='work_regions',
            field=models.TextField(blank=True, null=True, verbose_name='مناطق أو منطقة العمل'),
        ),
        migrations.AlterField(
            model_name='contactrequest',
            name='company_name',
            field=models.CharField(max_length=255, verbose_name='اسم الشركة'),
        ),
        migrations.AlterField(
            model_name='contactrequest',
            name='company_registration',
            field=models.FileField(upload_to='company_registration/', verbose_name='تسجيل الشركة'),
        ),
        migrations.AlterField(
            model_name='contactrequest',
            name='country_city',
            field=models.CharField(max_length=255, verbose_name='الدولة/المدينة'),
        ),
        migrations.AlterField(
            model_name='contactrequest',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='البريد الإلكتروني'),
        ),
        migrations.AlterField(
            model_name='contactrequest',
            name='know_us',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='كيف عرفت عنا؟'),
        ),
        migrations.AlterField(
            model_name='contactrequest',
            name='message',
            field=models.TextField(blank=True, null=True, verbose_name='الرسالة'),
        ),
        migrations.AlterField(
            model_name='contactrequest',
            name='number_required',
            field=models.PositiveIntegerField(verbose_name='عدد الدراجات المطلوبة'),
        ),
        migrations.AlterField(
            model_name='contactrequest',
            name='registration_num',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='أدخل رقم تسجيل صالح (10 أرقام).', regex='^[0-9]{10}$')], verbose_name='رقم التسجيل'),
        ),
        migrations.AlterField(
            model_name='contactrequest',
            name='selected_motorcycle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.motorcyclemodel', verbose_name='الدراجة النارية المختارة'),
        ),
    ]