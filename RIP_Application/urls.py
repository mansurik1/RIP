from django.contrib import admin
from django.urls import path, include
from flower_supplier_main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('flower_supplier_main.urls'))
]
