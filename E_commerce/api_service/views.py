from django.shortcuts import render
import requests
# Create your views here.
from rest_framework import status
from .serializers import ProducSerializer
from rest_framework.response import Response
from django.http import  JsonResponse
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from .models import *

@api_view(['POST','GET'])
def ProductApiView(request):
    if request.method == 'POST':
        serializer = ProducSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_502_BAD_GATEWAY)
        
    if request.method == 'GET':
        data = Product.object.all()
        serializer = ProducSerializer(data,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def  ProductDetailAPIView(request,company,productname):
    top = request.GET.get('top', 10)
    minPrice = request.GET.get('minPrice', 1)
    maxPrice = request.GET.get('maxPrice', 10000)
    url1 = 'http://20.244.56.144/products/auth'
    data = {
    "companyName": "goMart",
    "clientID": "b0df61d8-19d9-4d08-88ef-09840211483b",
    "clientSecret": "IQkevapeZJpOaEqS",
    "ownerName": "VISHVA",
    "ownerEmail": "vishva28sep@gmail.com",
    "rollNo": "721221106122"
    }
    response = requests.post(url1,json=data)
    print(response.json())
    url = f'http://20.244.56.144/products/companies/{company}/categories/{productname}/products'
    response_data = response.json()
    Token_type = response_data.get('toekn_type')
    token = response_data.get('access_token')
    headers = {
    'Authorization': f'{Token_type} {token}',
    'Content-Type': 'application/json'
    }
    params = {
        'top':top,
        'minPrice':minPrice,
        'maxPrice':maxPrice
    }
    response = requests.get(url,headers=headers,params=params)
    print(response)
    if request.method=='GET':
        if response.status_code==200:
            return Response(response.json())
        else:
            return Response({"error":"Not Found"})