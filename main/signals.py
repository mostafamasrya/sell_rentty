from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage
from django.conf import settings
from django.utils.html import format_html
from .models import ContactRequest
import mimetypes

@receiver(post_save, sender=ContactRequest)
def send_price_request_email(sender, instance, created, **kwargs):
    # if created:
    subject = 'طلب سعر جديد'
    message = format_html("""
    <html>
        <body>
            <h2>تفاصيل طلب السعر الجديد:</h2>
            <strong>عدد الدراجات المطلوب:</strong>
            <p>{number_required}</p>
            <hr>
            <strong>النوع:</strong>
            <p>{selected_motorcycle}</p>
            <hr>
            <strong>المنطقة:</strong>
            <p>{country_city}</p>
            <hr>
            <strong>اسم الشركة:</strong>
            <p>{company_name}</p>
            <hr>
            <strong>رقم السجل التجاري:</strong>
            <p>{registration_num}</p>
            <hr>
            <strong>البريد الإلكتروني:</strong>
            <p>{email}</p>
            <hr>
            <strong>كيف عرفت عنا:</strong>
            <p>{know_us}</p>
            <hr>
            <strong>الرسالة:</strong>
            <p>{message}</p>
        </body>
    </html>
    """.format(
        number_required=instance.number_required,
        selected_motorcycle=instance.selected_motorcycle.model,
        country_city=instance.country_city,
        company_name=instance.company_name,
        registration_num=instance.registration_num,
        email=instance.email,
        know_us=instance.know_us,
        message=instance.message or "لا توجد رسالة"
    ))

    recipient_list = [settings.RENTTY_EMAIL]

    email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, recipient_list)
    email.content_subtype = 'html'  # Set the content subtype to 'html'

    if instance.company_registration:
        mime_type, _ = mimetypes.guess_type(instance.company_registration.name)
        email.attach(instance.company_registration.name, instance.company_registration.read(), mime_type)

    email.send()
