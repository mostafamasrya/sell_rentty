from rest_framework import serializers
from main.models import ContactRequest, MotorcycleModel

class ContactRequestSerializer(serializers.ModelSerializer):
    knowUs = serializers.CharField(source='know_us', required=False, allow_null=True)
    companyRegistration = serializers.FileField(source='company_registration', required=True)
    companyOwnerId = serializers.FileField(source='owner_id', required=True)
    companyManagerId = serializers.FileField(source='manager_id', required=True)
    companyTransportLicense = serializers.FileField(source='transport_license', required=False)
    numberRequired = serializers.IntegerField(source='number_required')
    companyName = serializers.CharField(source='company_name')
    registrationNum = serializers.CharField(source='registration_num')
    countryCity = serializers.CharField(source='country_city')
    selectedMotorcycleId = serializers.PrimaryKeyRelatedField(
        source='selected_motorcycle', queryset=MotorcycleModel.objects.all()
    )
    representativesCount = serializers.IntegerField(source='representatives_count')
    workRegions = serializers.CharField(source='work_regions')
    deliveryAppName = serializers.CharField(source='delivery_app_name')
    monthlyDeposits = serializers.DecimalField(source='monthly_deposits', max_digits=12, decimal_places=2)

    class Meta:
        model = ContactRequest
        fields = [
            'knowUs', 'companyRegistration', 'message', 'numberRequired',
            'companyName', 'registrationNum', 'countryCity', 'email', 'mobile', 'selectedMotorcycleId',
            'companyOwnerId', 'companyManagerId', 'companyTransportLicense',
            'representativesCount', 'workRegions', 'deliveryAppName', 'monthlyDeposits'
        ]

    def create(self, validated_data):
        return ContactRequest.objects.create(**validated_data)
