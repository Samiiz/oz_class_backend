from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from bookmark.views import bookmark_index


def index(request):
    return HttpResponse("Hello, world")

def test(request):
    return HttpResponse("<h1>test</h1>")

def languages(request, lang):
    return HttpResponse(f'<h1>{lang}페이지 입니다.</h1>')

def number(request, num):
    return HttpResponse(f'<h1>{num}페이지 입니다.</h1>')



def gugu (request, num) :
    title = f'{num} 단 페이지 입니다.'
    gugudan = []
    for i in range(1, 10):
        gugudan.append(f'{num} x {i} = {num * i}')
    text = '</br>'.join(gugudan)
    return HttpResponse(f'<h1>{title}</h1> <p>{text}</p>')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('test/', test),
    path('lang/<lang>/', languages),
    path('number/<num>/', number),
    path('gugu/<int:num>/', gugu),
    path('bookmark/', bookmark_index),
]