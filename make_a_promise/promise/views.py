from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import PromiseModel
from .serializer import PromiseSerializer

class Promise_Api(ModelViewSet):
    queryset = PromiseModel.objects.all().order_by("id")
    serializer_class = PromiseSerializer
    

