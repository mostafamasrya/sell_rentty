from django.urls import path
from main.views import LandingPageView, SecondPageView, ThirdPageView, FourthPageView, FifthPageView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing-page-view'),
    path('request/1/', SecondPageView.as_view(), name='second-page-view'),
    path('request/2/', ThirdPageView.as_view(), name='third-page-view'),
    path('request/3/', FourthPageView.as_view(), name='fourth-page-view'),
    path('request/4/', FifthPageView.as_view(), name='fifth-page-view')
]
