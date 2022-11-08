from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from datetime import date


def model(field):
    site_menu = [
        {'menu_title': 'Каталог', 'menu_url': 'catalog'},
        {'menu_title': 'Доставка', 'menu_url': 'delivery'},
        {'menu_title': 'О нас', 'menu_url': 'about'},
        {'menu_title': 'Обратная связь', 'menu_url': 'feedback'}
    ]

    site_content = [
        {'title': 'Каталог', 'description': 'Здесь Вы можете ознакомиться с ассортиментом нашей продукции.',
         'photo': 'img/catalog.jpg'},
        {'title': 'Доставка', 'description': 'Мы осуществляем доставку по всей стране!',
         'photo': 'img/delivery.jpg'},
        {'title': 'О нас', 'description': 'Компания существует с 1992 года.',
         'photo': 'img/about.jpg'},
        {'title': 'Обратная связь', 'description': 'Оставьте Ваш отзыв. Спасибо!',
         'photo': 'img/feedback.jpg'}
    ]

    if field == 1:
        return site_menu
    else:
        return site_content


def index(request):
    return render(request, 'flower_supplier_main/index.html', {'menu': model(1),
                                                               'menu_title': 'Flower Stuff'})


def detailed(request, url):
    site_menu = model(1)
    site_content = model(2)
    result = dict()

    for i in range(len(site_menu)):
        if site_menu[i]['menu_url'] == url:
            result = site_content[i]

    return render(request, 'flower_supplier_main/detailed.html', {'menu': site_menu,
                                                                  'content': result})
