from django.db import models
from parler.models import TranslatableModel, TranslatedFields, TranslationDoesNotExist
from django.core.validators import RegexValidator

class MotorcycleModel(TranslatableModel):
    rental_price = models.DecimalField('سعر الإيجار', max_digits=10, decimal_places=2)
    translations = TranslatedFields(
        model = models.CharField('موديل', max_length=255),
        country_of_origin = models.CharField('بلد المنشأ', max_length=128),
    )
    image = models.ImageField('صورة', upload_to="motorcycle_images/")
    active = models.BooleanField('نشط', default=True)
    
    def __str__(self):
        try:
            return f'دراجة نارية {self.translations}'
        except TranslationDoesNotExist:
            return '-------'
    
    class Meta:
        verbose_name = 'موديل الدراجة النارية'
        verbose_name_plural = 'موديلات الدراجات النارية'
        
    @property
    def available(self):
        return True
    
    @property
    def ar_model(self):
        try:
            return self.translations.filter(language_code="ar").first().model
        except AttributeError :
            return self.model
        
    @property
    def ar_country_of_origin(self):
        try:
            return self.translations.filter(language_code="ar").first().country_of_origin
        except AttributeError :
            return self.country_of_origin


class Motorcycle(models.Model):
    motorcycle_model = models.ForeignKey(MotorcycleModel, on_delete=models.CASCADE, related_name="Motorcycles", verbose_name='موديل الدراجة النارية')
    chassis_number = models.CharField('رقم الهيكل', max_length=255, unique=True)
    rented = models.BooleanField('تم التأجير', default=False)
    
    def __str__(self):
        return f'{self.motorcycle_model.model} - {self.chassis_number}'

    class Meta:
        verbose_name = 'دراجة نارية'
        verbose_name_plural = 'دراجات نارية'


# class MotorcycleImage(models.Model):
#     motorcycle = models.ForeignKey(MotorcycleModel, on_delete=models.CASCADE, related_name="images", verbose_name='دراجة نارية')
#     image = models.ImageField('صورة', upload_to="motorcycle_images/")
#     main = models.BooleanField('رئيسي', default=False)

#     def save(self, *args, **kwargs):
#         if self.main:
#             # Ensure that no other image for the same motorcycle is set as main
#             MotorcycleImage.objects.filter(motorcycle=self.motorcycle, main=True).update(main=False)
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f'صورة لـ {self.motorcycle.model}'

#     class Meta:
#         verbose_name = 'صورة الدراجة النارية'
#         verbose_name_plural = 'صور الدراجات النارية'



class ContactRequest(models.Model):
    know_us = models.CharField("كيف عرفت عنا؟", max_length=255, blank=True, null=True)
    company_registration = models.FileField("تسجيل الشركة", upload_to="company_registration/")
    message = models.TextField("الرسالة", blank=True, null=True)
    number_required = models.PositiveIntegerField("عدد الدراجات المطلوبة")
    company_name = models.CharField("اسم الشركة", max_length=255)
    registration_num = models.CharField(
        "رقم التسجيل",
        max_length=10,
        validators=[RegexValidator(regex=r'^[0-9]{10}$', message="أدخل رقم تسجيل صالح (10 أرقام).")]
    )
    country_city = models.CharField("الدولة/المدينة", max_length=255)
    email = models.EmailField("البريد الإلكتروني")
    mobile = models.CharField("رقم الجوال", max_length=32, null=True)
    selected_motorcycle = models.ForeignKey(MotorcycleModel, verbose_name="الدراجة النارية المختارة", on_delete=models.SET_NULL, null=True)
    
    # New fields
    owner_id = models.FileField("هوية المالك", upload_to="owner_id/", blank=True, null=True)
    manager_id = models.FileField("هوية المدير", upload_to="manager_id/", blank=True, null=True)
    transport_license = models.FileField("ترخيص هيئة النقل", blank=True, null=True)
    representatives_count = models.PositiveIntegerField("عدد المناديب", blank=True, null=True)
    work_regions = models.TextField("مناطق أو منطقة العمل", blank=True, null=True)
    delivery_app_name = models.CharField("اسم تطبيق التوصيل", max_length=255, blank=True, null=True)
    monthly_deposits = models.DecimalField(
        "مبالغ الإيداعات الشهرية من تطبيقات التوصيل", 
        max_digits=12, 
        decimal_places=2,
        blank=True, null=True
    )
    
    # audit information
    created_at = models.DateTimeField("تاريخ الانشاء", auto_now_add=True)
    updated_at = models.DateTimeField("تاريخ التحديث", auto_now=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = "طلب اتصال"
        verbose_name_plural = "طلبات الاتصال"

