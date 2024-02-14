from django.urls import path
from . import views


urlpatterns = [
    path('<str:student_id>/<int:questionNum>', views.one_question),
    path('', views.main),
]