from django.urls import path
from main.apis.views import ContactRequestAPIView

urlpatterns = [
    path('send_pricing_request/', ContactRequestAPIView.as_view(), name='pricing-request-api'),
]
