from django.contrib import admin
from parler.admin import TranslatableAdmin
from main.models import MotorcycleModel, Motorcycle, ContactRequest

class MotorcycleModelAdmin(TranslatableAdmin):
    list_display = ('model', 'rental_price', 'country_of_origin', 'active')
    list_filter = ('active', 'translations__country_of_origin')
    search_fields = ('model', 'country_of_origin')
    fields = ('model', 'rental_price', 'country_of_origin', 'image', 'active')
    readonly_fields = ('available',)
    
    def available(self, obj):
        return obj.available()
    available.short_description = 'متاح'

admin.site.register(MotorcycleModel, MotorcycleModelAdmin)


class MotorcycleAdmin(admin.ModelAdmin):
    list_display = ('motorcycle_model', 'chassis_number', 'rented')
    list_filter = ('rented', 'motorcycle_model')
    search_fields = ('motorcycle_model__model', 'chassis_number')
    fields = ('motorcycle_model', 'chassis_number', 'rented')

admin.site.register(Motorcycle, MotorcycleAdmin)


class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'email', 'number_required', 'country_city', 'selected_motorcycle')
    search_fields = ('company_name', 'email', 'country_city', 'registration_num')
    list_filter = ('country_city', 'selected_motorcycle')
    readonly_fields = ('company_registration',)

    fieldsets = (
        ('بيانات الطلب', {
            'fields': (
                'know_us', 'company_name', 'registration_num', 'country_city', 
                'email', 'mobile', 'selected_motorcycle', 'number_required', 
                'message', 'representatives_count', 'work_regions', 
                'delivery_app_name', 'monthly_deposits'
            )
        }),
        ('الملفات', {
            'fields': (
                'company_registration', 'owner_id', 'manager_id', 
                'transport_license'
            )
        }),
        ('التواريخ', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        """Ensure audit fields are read-only."""
        return self.readonly_fields + ('created_at', 'updated_at')

admin.site.register(ContactRequest, ContactRequestAdmin)