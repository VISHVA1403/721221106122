from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests
# Create your views here.
from django.core.cache import cache
from rest_framework import status
from rest_framework.response import Response
from django.http import  JsonResponse
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from .models import *


@api_view(['GET'])
def AverageCalculater(request,qualifier):
    url = f'http://20.244.56.144/numbers/{qualifier}'
    response = requests.get(url)
    try :
        prev_state = cache.get('prev')
    except:
        prev_state =[]
    response_data = response.json()
    prev_state = cache.get('numbers')
    print(prev_state)
    cache.set(response_data.get('numbers'))
    
    if request.method=='GET':
        return Response(response.json())