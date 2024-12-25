from django.core.mail import send_mail
from django.conf import settings


class EmailService:
    def send_verification_code(self, email, code):
        send_mail(
            'رمز التحقق الخاص بك',
            f'رمز التحقق الخاص بك هو :{code}',
            settings.DEFAULT_FROM_EMAIL,
            [email]
        )
        
        
