from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.openapi import Response

from main.filters import ProjectFilter
from .models import *
from .serializers import *
from rest_framework import generics


class OrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class SubscribeView(generics.CreateAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscriptionSerializer


class TeamView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ProjectsView(generics.ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProjectFilter
    serializer_class = ProjectSerializer

    def get_queryset(self):
        service_name = self.kwargs.get('service_name')
        if service_name:
            return Projects.objects.filter(service__name=service_name)
        return Projects.objects.all()


class ServiceView(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer


class ServiceDetailView(generics.RetrieveAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer


class ServiceInfoView(generics.ListAPIView):
    queryset = ServiceInfo.objects.all()
    serializer_class = ServiceInfoSerializer


class ClientsFeedbackView(generics.ListAPIView):
    queryset = ClientsFeedback.objects.all()
    serializer_class = ClientsFeedbackSerializer


class CertificateView(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class FAQView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class FAQTypeView(generics.ListAPIView):
    queryset = FAQType.objects.all()
    serializer_class = FAQTypeSerializer


class WhyUsView(generics.ListAPIView):
    queryset = WhyUs.objects.all()
    serializer_class = WhyUsSerializer


class PartnersView(generics.ListAPIView):
    queryset = Partnership.objects.all()
    serializer_class = PartnerSerializer


class AboutView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializers


class PricePlanView(generics.ListAPIView):
    queryset = PricePlan.objects.all()
    serializer_class = PricePlanSerializer


class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class FeaturesListView(generics.ListAPIView):
    queryset =  Feature.objects.all()
    serializer_class = FeaturesSerializer
