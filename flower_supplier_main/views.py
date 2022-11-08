from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from datetime import date


# def greeting(request, number):
#     return HttpResponse(f'<h1>Добро пожаловать!</h1><p>Номер: {number}</p>')
#
#
# def hello(request):
#     return HttpResponse('Hello World!')


# def hello_students(request):
#     return render(request, 'index.html', {
#         'current_date': date.today()
#     })


site_menu = [
    {'menu_title': 'Каталог', 'id': 'catalog'},
    {'menu_title': 'Доставка', 'id': 'delivery'},
    {'menu_title': 'О нас', 'id': 'about'},
    {'menu_title': 'Обратная связь', 'id': 'feedback'}
]


def index(request):
    return render(request, 'flower_supplier_main/index.html', {'menu': site_menu, 'title': 'Flower Stuff'})


# def site(request, id):
#     return render(request, 'flower_supplier_main/site.html', {'menu': site_menu, 'id': id})


def catalog(request):
    return render(request, 'flower_supplier_main/catalog.html', {'menu': site_menu, 'id': id, 'title': 'Каталог'})

# def friendly_404(request, exception):
#     return HttpResponseNotFound('<h1>Страница не найдена</h1>')
