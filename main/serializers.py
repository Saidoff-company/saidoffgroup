from rest_framework import serializers
from .models import *


class WhyUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyUs
        fields = ['id', 'title', 'description']


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['id', 'information', 'image']


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ['id', 'icon', 'link']


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ['id', 'full_name', 'phone_number']


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partnership
        fields = ['id', 'image']


class ClientsFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientsFeedback
        fields = ['id', 'full_name', 'image', 'profession', 'message']


class ServiceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceInfo
        fields = ['id', 'title', 'image', 'description', 'services']


class ServiceSerializer(serializers.ModelSerializer):
    service_info = ServiceInfoSerializer(many=True, read_only=True)

    class Meta:
        model = Services
        fields = ['id', 'title', 'service_info']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'full_name', 'occupation', 'image']


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


class PricePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricePlan
        fields = ('title', 'limit_date', 'limit_user', 'features', 'price')


class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ('title', 'tick')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'title')
