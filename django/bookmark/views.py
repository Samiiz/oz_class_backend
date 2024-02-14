from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def bookmark_index(request):
    return render(
        request,
        'bookmark.html'
    )