# Create your views here.
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate
from user_app.serializers import *
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet,GenericViewSet
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from drf_yasg import openapi
from rest_framework.authentication import TokenAuthentication,BasicAuthentication
from user_app.models import CustomUser,StaffUser
from rest_framework.permissions import IsAuthenticated 
import random
import string
from complain_app.models import *

class Authen(GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserLoginSerializer
    authentication_classes = [TokenAuthentication,BasicAuthentication]
    @swagger_auto_schema(
        tags=['Auth'],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['version'],
            properties={
                'phone': openapi.Schema(type=openapi.TYPE_INTEGER),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
               
            },
        ),
    )
    @action(methods=["post"], detail=False, url_path="login", url_name="login",serializer_class = CustomUserLoginSerializer)
    def custom_user_login(self,request,*args,**kwargs):
        serializer = CustomUserLoginSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data['phone']
            password = serializer.validated_data['password']
            
            user = authenticate(request, phone=phone, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(tags=['Auth'])
    @action(methods=["post"], detail=False, url_path="logout", url_name="logout")
    def custom_user_logout(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            Token.objects.filter(user=user).delete()
            return Response({'message': 'Logged out successfully'})
        else:
            return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        
    @swagger_auto_schema(tags=['Auth'])
    @action(methods=["post"], detail=False, url_path="register", url_name="register", serializer_class = CustomRegisterserializer)
    def register(self,request,*args,**kwargs):
        serializer = CustomRegisterserializer(data=request.data)    
        if serializer.is_valid():
            serializer.save()
            phone = serializer.data['phone']
            otp = CustomUser.objects.get(phone=phone).otp
            message = f'An OTP has been sent to your phone number.'
            return Response({"message": message,"otp":otp}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(tags=['Auth'])
    @action(methods=["post"], detail=False, url_path="verify-otp", url_name="verify-otp")
    def verify_otp(self, request, *args, **kwargs):
        phone = request.data['phone']
        otp = request.data['otp']
        user = CustomUser.objects.get(phone=phone)
        if user.otp == otp:
            user.is_verified = True
            user.save()
            return Response({'message': 'OTP verified successfully'})
        else:
            user.is_verified = False
            user.save()
            return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(tags=['Auth'])
    @action(methods=["post"], detail=False, url_path="reset-password", url_name="reset-password")
    def reset_password(self, request, *args, **kwargs):
        phone = request.data['phone']
        characters = string.ascii_letters + string.digits  # Letters and digits
        otp = ''.join(random.choice(characters) for _ in range(6))
        try:
            user = CustomUser.objects.get(phone=phone)
            user.otp = otp
            user.save()
            return Response({'message': 'OTP sent successfully', 'otp': otp})
        except CustomUser.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(tags=['Auth'])
    @action(methods=["post"], detail=False, url_path="change-password", url_name="change-password")
    def change_password(self, request, *args, **kwargs):
        phone = request.data['phone']
        otp = request.data['otp']
        password = request.data['password']
        password_confirm = request.data['password_confirm']
        try:
            user = CustomUser.objects.get(phone=phone)
            if user.otp == otp:
                if password == password_confirm:
                    user.set_password(password)
                    user.save()
                    return Response({'message': 'Password changed successfully'})
                else:
                    return Response({'error': 'Confirm Password does not match'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)


class StaffUserView(ModelViewSet):
    serializer_class = StaffUserSerializer
    queryset = StaffUser.objects.all()
    authentication_classes = [TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]


    @swagger_auto_schema(tags=['Staff'])
    @action(methods=["get"], detail=False, url_path="self-profile", url_name="self-profile")
    def self_profile(self,request):
        user = request.user
        queryset = StaffUser.objects.filter(fk_user=user)
        serializer = StaffUserSerializer(queryset, many=True)
        return Response(serializer.data)
        
    
