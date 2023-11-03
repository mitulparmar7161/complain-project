from rest_framework import serializers
from complain_app.models import *

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class Complain_categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain_category
        fields = "__all__"

class Before_complain_resolved_fileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Before_complain_resolved_file
        fields = "__all__"

class After_complain_resolved_fileSerializer(serializers.ModelSerializer):
    class Meta:
        model = After_complain_resolved_file
        fields = "__all__"

class ComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain
        fields = "__all__"

class Complain_trakingSerializer(serializers.ModelSerializer):
    fk_complain = ComplainSerializer()
    class Meta:
        model = Complain_traking
        fields = "__all__"



class ComplainSerializerForUserUpload(serializers.ModelSerializer):
    class Meta:
        model = Complain
        fields = "__all__"