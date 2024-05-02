from django.db.models import Q
from goods.models import Products

def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    # Разделение запроса на отдельные слова и фильтрация коротких слов
    keywords = [word for word in query.split() if len(word) > 2]

    # Создание Q-объектов для поиска по полям name и description
    q_objects = Q()
    for token in keywords:
        q_objects |= Q(description__icontains=token)
        q_objects |= Q(name__icontains=token)

    # Фильтрация по тем строкам, где найдены соответствия
    result = Products.objects.filter(q_objects)

    return result
