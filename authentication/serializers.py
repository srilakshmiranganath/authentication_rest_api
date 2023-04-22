from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

class VerifyResultSerializer(serializers.Serializer):
    str1 = serializers.CharField()
    str2 = serializers.CharField()
    result = serializers.CharField()