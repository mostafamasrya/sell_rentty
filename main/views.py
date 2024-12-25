from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import serializers
from main.models import MotorcycleModel


class MotorcycleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotorcycleModel
        fields = '__all__'

class LandingPageView(TemplateView):
    template_name = 'website/landing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # query = MotorcycleModel.objects.filter(active=True)
        # serializer = MotorcycleModelSerializer(query,many=True)
        context['motorcycle_brand_list'] = MotorcycleModel.objects.filter(active=True)


        return context



class SecondPageView(TemplateView):
    template_name = 'website/sec-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['motorcycle_brand_list'] = MotorcycleModel.objects.filter(active=True)

        return context
    
    
class ThirdPageView(TemplateView):
    template_name = 'website/third-page.html'


class FourthPageView(TemplateView):
    template_name = 'website/fourth-page.html'
    

class FifthPageView(TemplateView):
    template_name = 'website/fifth-page.html'




class LandingPageView2(TemplateView):
    template_name = 'website/landing2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['motorcycle_brand_list'] = MotorcycleModel.objects.filter(active=True)

        return context