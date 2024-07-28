from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    context = {
        'title': 'MedIBox - Главная',
        'content': 'Веб-интерфейс управления таблетницами MedIBox',
        'text_on_page': 'Хехе',
    }

    return render(request, "main/index.html", context)


def about(request):

    context = {
        'title': 'MedIBox - О нас',
        'content': 'О нас',
        'text_on_page': 'Тут нечего сказать...'
    }

    return render(request, "main/about.html", context)


def contact(request):

    context = {
        'title': 'MedIBox - Контакты',
        'content': 'Наши контакты',
        'text_on_page': 'Хер вам, а не контакты'
    }

    return render(request, "main/contact.html", context)