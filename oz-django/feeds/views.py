from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializers import FeedSerializer
from .models import Feed
# Create your views here

class Feeds(APIView):
    # 전체 게시글 조회
    def get(self, request):
        feeds = Feed.objects.all()
        
        # 객체 -> JSON (시리얼 라이즈/직렬화)

        serializer = FeedSerializer(feeds, many=True)

        return Response(serializer.data)

    # 게시글 생성
    def post(self, request):
        # 역직렬화 : JSON -> object
        serializer = FeedSerializer(data=request.data)

        if serializer.is_valid():
            feed = serializer.save(user=request.user)

            serializer = FeedSerializer(feed)

            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class FeedDetail(APIView):
    def get_object(self, feed_id):
        try:
            return Feed.objects.get(id=feed_id)
        except Feed.DoesNotExist:
            raise NotFound
        
    def get(self, request, feed_id):
        feed = self.get_object(feed_id)
        
        serializer = FeedSerializer(feed)

        return Response(serializer.data)





# def show_feed(request):
#     return HttpResponse("Show Feeds")

# def all_feed(request):
#     return HttpResponse("All Feeds")

# def one_feed(request, feed_id, feed_content):
#     return HttpResponse(f"피드번호 : {feed_id} <br/> 피드내용 : {feed_content}")