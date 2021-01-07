
from rest_framework import serializers
from .models import CustomAdminData


class CustomAdminSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomAdminData
        fields = ['adminRollNo','adminPin']