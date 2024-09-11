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
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class CertificateView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class FAQView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class FAQTypeView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class WhyUsView(generics.ListAPIView):
    queryset = WhyUs.objects.all()
    serializer_class = WhyUsSerializer


class PartnersView(generics.ListAPIView):
    queryset = Partnership.objects.all()
    serializer_class = PartnerSerializer


class AboutView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializers
