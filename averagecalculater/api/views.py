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
    
    
    if request.method=='GET':
        url = f'http://20.244.56.144/numbers/{qualifier}'
        response = requests.get(url)
        try :
            prev_state = cache.get('prev')
        except:
            prev_state =[]
        response_data = response.json()
        prev_state = cache.get('prev_state')
        # cache.set('prev_state',response_data.get('numbers'))
        numbers = response_data.get('numbers')
        curr_state = numbers.copy()
        try:
            for vall in prev_state:
                if vall in curr_state:
                    index = curr_state.index(vall)
                    curr_state.pop(index)
        finally:
            avg = sum(curr_state)/len(curr_state)
            data = {
                "numbers":numbers,
        "windowPrevState":prev_state if prev_state else [],
                "windowCurrState":curr_state,
                "avg":avg
            }
            cache.set('prev_state',curr_state)
            return Response(data=data)