from rest_framework import serializers
from .models import *


class WhyUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyUs
        fields = '__all__'


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partnership
        fields = '__all__'


class ClientsFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientsFeedback
        fields = '__all__'


class ServiceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceInfo
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    service_info = ServiceInfoSerializer(many=True, read_only=True)

    class Meta:
        model = Services
        fields = ['id', 'title', 'service_info']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)

    class Meta:
        model = Projects
        fields = '__all__'


class FAQTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQType
        fields = '__all__'


class FAQSerializer(serializers.ModelSerializer):
    type = FAQTypeSerializer(read_only=True)

    class Meta:
        model = FAQ
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)
    class Meta:
        model = Order
        fields = '__all__'


class AboutSerializers(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
