from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.serializers import HomesSerializer
from homes.models import Home


class HomesApi(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Home.objects.all()
    serializer_class = HomesSerializer
    # http_method_names = ['get']
