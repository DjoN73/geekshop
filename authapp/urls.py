from django.urls import path
from authapp.views import login, logout, register, edit
from authapp.utils import verify

app_name = 'authapp'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
    path('path/', path, name='path'),
    path('verify/<str:email>/<str:activation_key>/', verify, name='verify'),
]
