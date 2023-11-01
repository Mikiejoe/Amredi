# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,UpdateAPIView,RetrieveAPIView
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from sms.sms import send_authentication_code
from random import random
from decouple import config


from .models import Users

class CreateUser(CreateAPIView):
    serializer_class = UserSerializer
    queryset = Users.objects.all()
    
@api_view(['POST'])
def createuser(request):
    data = request.data
    serializer = UserSerializer(data=data)
    print(data)
    phone = request.POST['phone']
    print(request.POST)
    phone = data['phone']
    code = random()
    print(config('api_key'))
    code = str(code).split('.')[-1]
    send_authentication_code(phone_number = '254740510778',verification_code = '2345')
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)