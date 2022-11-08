from django.urls import path
from flower_supplier_main import views

urlpatterns = [
    # path('<int:number>/', views.greeting),
    # path('hello/', views.hello)
    # path('hello-students/', views.hello_students)

    path('', views.index),
    path('catalog/', views.catalog),
    path('<str:id>/', views.catalog, name='element_url')
]
