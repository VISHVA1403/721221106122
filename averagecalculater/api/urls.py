from django.urls import path
from .views import *

urlpatterns = [
    path('numbers/<str:qualifier>',AverageCalculater),

]