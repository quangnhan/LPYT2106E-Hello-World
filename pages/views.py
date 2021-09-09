from django.http import HttpResponse


def home_page(request):
    return HttpResponse('Home Page')


def about_page(request):
    return HttpResponse('About Page')
