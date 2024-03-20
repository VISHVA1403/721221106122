from django.urls import path
from .views import *

urlpatterns = [
    path('products/companies/<str:company>/categories/<str:productname>/products',ProductDetailAPIView),

]