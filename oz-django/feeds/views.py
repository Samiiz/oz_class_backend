from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def show_feed(request):
    return HttpResponse("Show Feeds")

def all_feed(request):
    return HttpResponse("All Feeds")

def one_feed(request, feed_id, feed_content):
    return HttpResponse(f"피드번호 : {feed_id} <br/> 피드내용 : {feed_content}")