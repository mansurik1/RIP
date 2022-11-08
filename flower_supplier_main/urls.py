from django.urls import path
from flower_supplier_main import views

urlpatterns = [
    path('', views.index),
    path('<str:url>/', views.detailed, name='element_url')
]
