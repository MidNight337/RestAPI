"""drfsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from atexit import register
from django.contrib import admin
from django.urls import path, include, re_path
from women.views import *
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView




#routes - это список наших маршрутов
# class MyCustomRouter(routers.SimpleRouter): #создание собственного роутера, наследуемся от самого простого класса роутеров
#     routes = [
#         routers.Route(url=r'^{prefix}$', # url - это щаблон наших маршрутов
#                       mapping={'get': 'list'}, # связывает тип запроса с соответствующим методом viewset'a
#                       name ='{basename}-list', # определяет название маршрута
#                       detail = False, # False - покажет список, True - покажет отдельную запись
#                       initkwargs={'suffix' : 'List'}), #отдельные аргументы, которые будут передаваться при срабатывании маршрута
#     #Считался список статей
#         routers.Route(url=r'^{prefix}/{lookup}$',
#                       mapping={'get':'retrieve'},
#                       name ='{basename}-detail',
#                       detail=True,
#                       initkwargs = {'suffix' : 'Detail'})
#     #Читает конкретную статью по ее идентификатору
#     ]

# router = MyCustomRouter()
# router.register(r'women', WomenViewSet, basename= 'women')
# print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/women', WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),
    path('api/v1/token/verify', TokenVerifyView.as_view(), name = 'token_verify'),
]    
    #http://127.0.0.1:8000/api/v1/women
    #path('api/v1/womenlist/', WomenViewSet.as_view({'get' : 'list'})),# связываем маршруты с классом представлений WomenAPIList
    #path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put' : 'update'})),# <int:pk> будет показывать какую запись собираемся поменять   

