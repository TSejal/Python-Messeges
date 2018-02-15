from django.shortcuts import render
from testModel.models import *
from testModel.serializers import *
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q
# Create your views here.


@api_view(['GET'])
def question_14(request):
    result = Message.objects.all().order_by('-created_on')
    serializer = MessageSerializer(result, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def question_15(request):
    result = Message.objects.all()
    result_1st5 = result[:5]
    result_6to10 = result[5:10]
    serializer1 = MessageSerializer(result_1st5, many = True)
    serializer2 = MessageSerializer(result_6to10, many = True)
    return Response({"1st 5 records":serializer1.data,"6 to 10 records":serializer2.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def question_16(request):
    result = Message.objects.filter(message__icontains = "Good Morning")
    serializer = MessageSerializer(result, many = True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['GET'])
def question_17(request):
    result = Message.objects.filter(message = "")
    serializer = MessageSerializer(result, many = True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def question_18(request):
    result = Message.objects.exclude(message = 'Nice')
    serializer = MessageSerializer(result, many = True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def question_19(request):
    result = Message.objects.filter(message__startswith = 'who')
    serializer = MessageSerializer(result, many = True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def question_20(request):
    result = Message.objects.filter(message_from__first_name = 'Pratik')
    serializer = MessageSerializer(result, many = True)
    return Response(serializer.data, status=status.HTTP_200_OK)

