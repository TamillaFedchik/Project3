from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):

    
    context: dict = {
        'title': 'Coffee - Главная',
        'content': "Site-TasteBucks",
    }

    return render(request, 'main/index.html', context)


def about(request):
    context: dict = {
        'title': 'Coffee - О нас',
        'content': "Мы",
        'text_on_page': "Мы очень старались над его созданием."

    }

    return render(request, 'main/about.html', context)
