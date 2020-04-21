from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from api.models import BloodCenter
from api.permissions import ReadOnly
from api.serializers import BloodCenterSerializer


class BloodCenterListView(generics.ListAPIView):
    http_method_names = ['get']
    serializer_class = BloodCenterSerializer
    queryset = BloodCenter.objects.all()
    permission_classes = [ReadOnly]