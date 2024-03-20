from rest_framework import serializers
from .models import Company,Product
class CompanyRegister(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class ProducSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'