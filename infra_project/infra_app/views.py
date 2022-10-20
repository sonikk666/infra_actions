from django.http import HttpResponse


def index(request):
    return HttpResponse('Еле-еле, но У меня получилось!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
