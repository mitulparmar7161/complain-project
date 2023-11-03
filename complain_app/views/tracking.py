from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from complain_app.models import *
from complain_app.serializers import *

class TrackingView(viewsets.ModelViewSet):
    serializer_class = Complain_trakingSerializer
    queryset = Complain_traking.objects.all()

    @swagger_auto_schema(tags=['Tracking'])
    def list(self,request,*args,**kwargs):
        pass




    @swagger_auto_schema(auto_schema=None)
    def create(self, request, *args, **kwargs):
        pass
    @swagger_auto_schema(auto_schema=None)
    def retrieve(self, request, *args, **kwargs):
        pass
    @swagger_auto_schema(auto_schema=None)
    def update(self, request, *args, **kwargs):
        pass
    @swagger_auto_schema(auto_schema=None)
    def partial_update(self, request, *args, **kwargs):
        pass
    @swagger_auto_schema(auto_schema=None)
    def destroy(self, request, *args, **kwargs):
        pass