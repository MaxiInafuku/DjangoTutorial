from django.urls import path
from . import views 

urlpatterns = [
    path('', views.test, name='test'), #if empty, it means that we're at the main site. name = is the "id" to be recognized later.
    path('counter', views.counter, name='counter'),
    path('index', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login')
]
