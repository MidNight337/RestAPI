from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from .models import Women, Category
from .serializers import WomenSerializer


class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()# eсли убираем queryset, то в urls router.register добавляем basename = ...
    serializer_class = WomenSerializer
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')# получаем ключ pk из колекции kwargs c помощью get 'pk'

        if not pk: # если такого ключа нет, то возвращаем список записей
          return Women.objects.all()[:3]

        return Women.objects.filter(pk=pk) #если проверка не прошла вернем конкретную запись т.к. pk=pk
  

#декоратор actions оборачивает модели women в категории добавляет новые нестандартные маршруты в ViewSet
# detail = False дает возможность показать все категории, но не 1 конкретную
    @action(methods=['get'], detail = True)
    def category(self, requests, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats' : cats.name})












# class WomenAPIList (generics.ListCreateAPIView): # Возвращает список записей по GET-запросу и добавляет новые записи по POST-запросу
#     queryset = Women.objects.all()#ссылается на список записей возвращ клиенту
#     serializer_class = WomenSerializer # сериализатор который применяем к queryset

# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
    
# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

# class WomenAPIView(APIView):
#     def get(self, request):
#         w = Women.objects.all()
#         return Response({"posts" : WomenSerializer(w, many = True).data})


#     def post(self, request):  #POST-запрос
#         serializer = WomenSerializer(data = request.data) #здесь входные данные преобразованы в объект serializator
#         serializer.is_valid(raise_exception = True) #проверка данных, формирование словарая validated.data
#         serializer.save() #Сохранение данных после их добавления в serializers

#         return Response({'post' :  serializer.data}) # Возврат добавленных данных

#     """*args - позиционные аргументы
#       **kwargs -  именованные аргументы"""
#     def put(self, request, *args, **kwargs): # функция для обновдения данных
#         pk = kwargs.get('pk', None) # с помощью  словаря**kwargs обращение к нужной статье если нет pk - возвращаем None 
#         if not pk: #если нет ключа pk в коллекции **kwargs
#             return Response({"error" : "Method PUT is NOT ALLOWED"}) #возврат ответа - если нет ключа, то данные изменить невозможно

#         try:
#             instanse = Women.objects.get(pk=pk) #пытаемся взять запись из модели Women
#         except:# Но если не можем взять указанную запись(например не верный ПК)
#             return Response({"error": "Object does not exist"})# объект не найден
       
#        #instanse указывает, какой из методов в serializers нам нужно вызвать

#         serializer = WomenSerializer(data = request.data, instance=instanse) # передача в качестве аргумента request_data, и объекта instanse, который бедем менять
#         serializer.is_valid(raise_exception=True)# проверка данных (raise_exeprion=True - означает, что мы можем переопределить стиль ответов на ошибки валидации Глобально)
#         serializer.save() # save() вызывает метод UPDATE из serializers, сохраняет обновленные данные
#         return Response({"post" : serializer.data})
        
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error" : "Method DELETE not allowed"})
        
#         try:
#             instanse = Women.objects.delete(pk=pk)
#         except:
#             return Response({"error" : "Object does not exist"})

#         #serializer = self.get_object(pk)
#         #serializer.is_deleted = True
#         #serializer.save()
#         return Response({"post" : "DELETED post" + str(pk)})
#class WomenAPIView(generics.ListAPIView):
 #   queryset = Women.objects.all()
  #  serializer_class = WomenSerializer


# Create your views here.
