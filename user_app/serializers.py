from rest_framework import serializers
from user_app.models import CustomUser
from user_app.serializers import *
from user_app.models import CustomUser,StaffUser
import random
import string
from complain_app.serializers import OrganizationSerializer,DepartmentSerializer
class CustomUserLoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField(write_only=True)

class CustomRegisterserializer(serializers.Serializer):
    email=serializers.EmailField()
    phone=serializers.IntegerField()
    password=serializers.CharField(write_only=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    class Meta:
        model = CustomUser
        fielsd = '__all__'
        extra_kwargs = {
            'ProfileImage': {'required': False},
            'City': {'required': False}
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('Password Does Not Match')
        if len(str(data['phone'])) != 10:
            raise serializers.ValidationError('Please Enter Valid Phone Number')
        if CustomUser.objects.filter(phone=data['phone']).exists():
            raise serializers.ValidationError('Phone Number Already Exists')
        if CustomUser.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError('Email Already Exists')
        return data
        
    def create(self, validated_data):
        characters = string.ascii_letters + string.digits  # Letters and digits
        otp = ''.join(random.choice(characters) for _ in range(6))

        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            phone=validated_data['phone'],
            password=validated_data['password'],
            otp=otp
        )
        return user

class StaffUserSerializer(serializers.ModelSerializer):
    fk_organization = OrganizationSerializer()
    fk_department = DepartmentSerializer()
    class Meta:
        model = StaffUser
        fields = '__all__'