from django.shortcuts import render
from django.http import HttpResponse
from datetime import date


def model(variant, number_of_entries_custom=0):
    output = list()

    if variant == 'topics':
        output = [
            {'title': 'Каталог продукции', 'url': 'catalog'},
            {'title': 'Условия доставки/самовывоза', 'url': 'delivery'},
            {'title': 'Контакты отдела продаж', 'url': 'sales'}
        ]
    elif variant == 'items':
        output = [
                {'title': 'Роза', 'price': 70, 'available_quantity': 13, 'id': 1},
                {'title': 'Альстромерия', 'price': 65, 'available_quantity': 0, 'id': 2},
                {'title': 'Лилия', 'price': 91, 'available_quantity': 43, 'id': 3},
                {'title': 'Тюльпан', 'price': 34, 'available_quantity': 1, 'id': 4},
                {'title': 'Хризантема', 'price': 66, 'available_quantity': 13, 'id': 5},
                {'title': 'Пион', 'price': 75, 'available_quantity': 54, 'id': 6},
                {'title': 'Гербера', 'price': 54, 'available_quantity': 9, 'id': 7},
                {'title': 'Анемон', 'price': 61, 'available_quantity': 5, 'id': 8},
                {'title': 'Астра', 'price': 44, 'available_quantity': 121, 'id': 9},
                {'title': 'Ландыш', 'price': 39, 'available_quantity': 0, 'id': 10},
            ]
    elif variant == 'images_paths':
        output = [
            {'path': '/img/rose.jpg', 'id': 1},
            {'path': '/img/alstromeria.jpg', 'id': 2},
            {'path': '/img/lily.jpg', 'id': 3},
            {'path': '/img/tulip.jpg', 'id': 4},
            {'path': '/img/chrysanthemum.jpg', 'id': 5},
            {'path': '/img/peony.jpg', 'id': 6},
            {'path': '/img/gerbera.jpg', 'id': 7},
            {'path': '/img/anemone.jpg', 'id': 8},
            {'path': '/img/aster.jpg', 'id': 9},
            {'path': '/img/lily_of_the_valley.jpeg', 'id': 10},
        ]

    number_of_entries = len(output)
    try:
        number_of_entries_custom = int(number_of_entries_custom)
        if 0 < number_of_entries_custom <= len(output):
            number_of_entries = number_of_entries_custom
    finally:
        return output[0:number_of_entries]


def main_page(request):
    return render(request, 'RIP_lab/index.html', {
        'topics': model('topics')
    })


def enter_topic(request, url):
    if url == 'catalog':
        return render(request, 'RIP_lab/catalog.html', {
            'items': model('items')
        })
    elif url == 'delivery':
        return render(request, 'RIP_lab/delivery.html')
    elif url == 'sales':
        return render(request, 'RIP_lab/sales.html')

    return HttpResponse('Пусто')


def send_text(request):
    input_text = request.POST['text']
    return render(request, 'RIP_lab/catalog.html', {
        'items': model('items', input_text)
    })


def get_catalog_item(request, item_id):
    return render(request, 'RIP_lab/item.html', {
        'id': item_id,
        'item': model('items')[item_id - 1],
        'image_path': model('images_paths')[item_id - 1]
    })
