from django.shortcuts import render
from django.http import HttpResponse
from datetime import date


number_of_entries_custom = 10


def model(variant, number_of_entries_custom):
    output = list()
    if variant == 'topics':
        output = [
            {'title': 'Каталог продукции', 'url': 'catalog'},
            {'title': 'Условия доставки/самовывоза', 'url': 'delivery'},
            {'title': 'Контакты отдела продаж', 'url': 'sales'}
        ]
    if variant == 'items':
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
    if variant == 'images_paths':
        output = [
            {'path': 'https://i.artfile.me/wallpaper/28-08-2013/800x600/cvety-rozy-rozovyj-krasavica-748252.jpg', 'id': 1},
            {'path': 'https://www.nature-and-garden.com/wp-content/uploads/2017/09/alstromeria-1024x678.jpg', 'id': 2},
            {'path': 'https://cloverflowers.ru/wp-content/uploads/2020/10/liliya_orange.jpg', 'id': 3},
            {'path': 'https://img2.goodfon.ru/original/1024x768/6/67/krasnyy-tyulpan-kapli.jpg', 'id': 4},
            {'path': 'https://wallbox.ru/resize/640x480/wallpapers/main/201308/xrizantema-cvetok-foto-0debaad.jpg', 'id': 5},
            {'path': 'https://dubabah.club/uploads/posts/2023-01/thumbs/1673618025_dubabah-club-p-bolshie-kusti-pionov-krasivo-58.jpg', 'id': 6},
            {'path': 'https://img4.goodfon.ru/original/800x480/7/47/red-gerberas-macro-krasnaia-gerbera-makro.jpg', 'id': 7},
            {'path': 'https://i.artfile.me/wallpaper/02-07-2016/1280x960/cvety-anemony--son-trava-makro-anemon-1054496.jpg', 'id': 8},
            {'path': 'https://klike.net/uploads/posts/2022-09/1664279202_j-42.jpg', 'id': 9},
            {'path': 'https://shopikk.ru/wp-content/uploads/1/f/3/1f3e0b79b9db265d084099fffca128f6.jpeg', 'id': 10},
        ]
    number_of_entries = len(output)
    if number_of_entries_custom != 0 and 0 < number_of_entries_custom <= len(output):
        number_of_entries = number_of_entries_custom

    return output[0:number_of_entries]


def main_page(request):
    return render(request, 'RIP_lab/index.html', {
        'topics': model('topics', 0)
    })


def enter_topic(request, url):
    if url == 'catalog':
        return render(request, 'RIP_lab/catalog.html', {
            'items': model('items', 0)
        })
    return HttpResponse('Пусто')


def get_catalog_item(request, item_id):
    return render(request, 'RIP_lab/item.html', {
        'id': item_id,
        'item': model('items', 0)[item_id - 1],
        'image_path': model('images_paths', 0)[item_id - 1]
    })


def send_text(request):
    input_text = request.POST['text']
    return render(request, 'RIP_lab/catalog.html', {
        'items': model('items', int(input_text))
    })
