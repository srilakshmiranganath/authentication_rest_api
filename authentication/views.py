from django.shortcuts import render
from .serializers import *
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from authentication import models

# Create your views here.

@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def verify(request):
    if request.method == 'POST':
        string1 = 'hello'
        string2 = str(request.data['str2'])
        if string1 == string2:
            answer = "Match"
        else:
            answer = "Not Match"

        r = models.VerifyResult()
        r.str1 = string1
        r.str2 = string2
        r.result = answer
        serializer = VerifyResultSerializer(r)

        return Response({"message" : "Verification Completed", "VerifyResult" : serializer.data})
    return Response({"message" : "To perform string verification, do a POST request to this url in the json format {str2 : hi} and you will get results in the format {'message' : 'Verification Completed', 'VerifyResult': {str1 : 'hello', str2 = 'hi', result : 'Not Match'}}"})        