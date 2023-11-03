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


class ComplainView(viewsets.ModelViewSet):
    serializer_class = ComplainSerializerForUserUpload
    queryset = Complain.objects.all()

    @swagger_auto_schema(tags=['complain'])
    def create(self, request, *args, **kwargs):
        user_id = request.user.id
        request.data['fk_consumer'] = user_id
        serializer = ComplainSerializerForUserUpload(data=request.data)
        if serializer.is_valid():
            serializer.save()
            tracking = Complain_traking.objects.create(
                fk_complain_id=serializer.instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(tags=['complain'],operation_description="My complais")
    @action(methods=['get'],detail=False,url_path='my-complains',url_name='my-complains',permission_classes=[IsAuthenticated],authentication_classes=[TokenAuthentication])
    def my_complains(self,request):
        user = request.user
        complains = Complain.objects.filter(fk_consumer=user)
        serializer = ComplainSerializer(complains,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    @swagger_auto_schema(tags=['complain'],operation_description="Complain Status")
    def retrieve(self, request, *args, **kwargs):
        user_id = request.user.id
        complain_id = kwargs['pk']
        try:
            tracking = Complain_traking.objects.filter(fk_complain=complain_id)
            serializer = Complain_trakingSerializer(tracking,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)

        except:
            return Response({"message":"Complain Not Found"},status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(auto_schema=None)
    def list(self,request,*args,**kwargs):
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
            

class ComplainCategoryView(viewsets.ModelViewSet):
    serializer_class = Complain_categorySerializer
    queryset = Complain_category.objects.all()


    @swagger_auto_schema(tags=['complain-category'],operation_description="Complain Category")
    def list(self,request,*args,**kwargs):

        category = Complain_category.objects.all()
        serializer = Complain_categorySerializer(category,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    @swagger_auto_schema(auto_schema=None)
    def partial_update(self, request, *args, **kwargs):
        pass

    @swagger_auto_schema(auto_schema=None)
    def create(self, request, *args, **kwargs): 
        pass

    @swagger_auto_schema(auto_schema=None)
    def update(self, request, *args, **kwargs):
        pass

    @swagger_auto_schema(auto_schema=None)
    def destroy(self, request, *args, **kwargs):
        pass

    @swagger_auto_schema(auto_schema=None)
    def retrieve(self, request, *args, **kwargs):
        pass