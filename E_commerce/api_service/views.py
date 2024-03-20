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
    url = f'http://20.244.56.144/products/companies/{company}/catogories/{productname}/products'
    headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzEwOTEzNjI3LCJpYXQiOjE3MTA5MTMzMjcsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6ImIwZGY2MWQ4LTE5ZDktNGQwOC04OGVmLTA5ODQwMjExNDgzYiIsInN1YiI6InZpc2h2YTI4c2VwQGdtYWlsLmNvbSJ9LCJjb21wYW55TmFtZSI6ImdvTWFydCIsImNsaWVudElEIjoiYjBkZjYxZDgtMTlkOS00ZDA4LTg4ZWYtMDk4NDAyMTE0ODNiIiwiY2xpZW50U2VjcmV0IjoiSVFrZXZhcGVaSnBPYUVxUyIsIm93bmVyTmFtZSI6IlZJU0hWQSIsIm93bmVyRW1haWwiOiJ2aXNodmEyOHNlcEBnbWFpbC5jb20iLCJyb2xsTm8iOiI3MjEyMjExMDYxMjIifQ.saFbc78TDF7VB9x8d5yBq9ra7ldx5lIZw5g_D420hiM',
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
        if response.status_code!=200:
            return Response(response)
        else:
            return Response({"error":"Not Found"})