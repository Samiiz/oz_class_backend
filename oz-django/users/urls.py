from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns =[
    path('', views.Users.as_view()),
    path('myinfo/', views.MyInfo.as_view()),

    # Authentication
    path('getToken', obtain_auth_token),
    path('login', views.Login.as_view()),
    path('logout', views.Logout.as_view()),

    # JWT Authentication
    path('login/jwt', views.JWTLogin.as_view()),
    path('login/jwt/info', views.UserDetailView.as_view()),

    # Simppl JWT Authentication
    path('login/simpleJWT', TokenObtainPairView.as_view()),
    path('login/simpleJWT/refresh', TokenRefreshView.as_view()),
    path('login/simpleJWT/verify', TokenVerifyView.as_view()),
]

# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwOTYwMzUxNiwiaWF0IjoxNzA4MzkzOTE2LCJqdGkiOiI4M2I5NDQ3ZjgzNmU0NjIxODA0ZmE4NTI1ZTg2MTEyOCIsInVzZXJfaWQiOjF9.V4H5GGrhdSS4UW7UPxNj8ofsgfjvTPtfKIdnt6XtrGI",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA4Mzk3NTE2LCJpYXQiOjE3MDgzOTM5MTYsImp0aSI6IjUxNWEzN2IyZjM1MzRlMDk4YTFmMmE1M2Q5ZDFlZmJmIiwidXNlcl9pZCI6MX0.4QZUcp8y0SOU0VW_POYHC3uNDezquhBDwD0TUv-oAq4"
# }