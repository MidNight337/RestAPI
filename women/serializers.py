import io

from rest_framework import serializers
from .models import Women
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


#class WomenModel():
#    def __init__(self, title,content):
#        self.title = title
#        self.content = content

class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women # тут переменная model ссылается на Объект Women
        fields = '__all__' # Указываем ВСЕ поля которые будут возвращаться клиенту
        """ class Meta заменяет нам создание полей, а так же функции create, update u delete"""

#     title = serializers.CharField(max_length =255)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only = True)
#     time_update = serializers.DateTimeField(read_only = True)
#     is_published = serializers.BooleanField(default = True)
#     cat_id = serializers.IntegerField()

# def create(self, validated_data):# передача в словарь **validated data данных с POST запроса
#     return Women.objects.create(**validated_data)# добавление новых данных в таблицу Women

# def update(self, instanse, validated_data):# instanse - это ссылка на модель Women
#     #validated.data - это словарь из проверенных данных,которые нужно  изменить в БД
#     instanse.title = validated_data.get("title", instanse.title)
#     instanse.content = validated_data.get("content", instanse.content)
#     instanse.time_update = validated_data.get("time_update", instanse.time_update)
#     instanse.is_published = validated_data.get("is_published", instanse.is_published)
#     instanse.save() # cохранение изменений в БД
#     return instanse # ОБЯЗАТЕЛЬНО вернуть объект instanse


#def encode():
#    model = WomenModel('Angelina Jolie', 'Content: Angelina Jolie')
#    model_sr = WomenSerializer(model)
#    print(model_sr, type(model_sr.data), sep ='\n')
#  json = JSONRenderer().render(model_sr.data)
#   print(json)

#def decode():
#    stream = io.ByteIO(b'{"title" : "Angelina Jolie", "Content: Angelina Jolie"}')
#    data = JSONParser().parse(stream)
#    serializer = WomenSerializer(data=data)
#    serializer.is_valid()
#    print(serializer.validated_data)


