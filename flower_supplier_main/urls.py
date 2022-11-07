from django.urls import path
from flower_supplier_main import views

urlpatterns = [
    path('<int:number>/', views.greeting),
    path('hello/', views.hello)
]
