from django.urls import path
from .views import *

urlpatterns = [
    path('products/companies/<str:company>/catogories/<str:productname>/products',ProductDetailAPIView),

]