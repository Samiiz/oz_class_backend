from django.urls import path
from . import views

urlpatterns = [
    # 1차
    # path('', views.show_feed),
    # path('all', views.all_feed),
    # path('<int:feed_id>/<str:feed_content>', views.one_feed),

    # 2차
    path('', views.Feeds.as_view()),
    path('<int:feed_id>/', views.FeedDetail.as_view()),
]