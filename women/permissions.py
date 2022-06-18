#Свой класс для установки разрешений!

from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission): # создание класса где админ может удалять а др. нет
    def has_permission(self, request, view): # переопределение метода has_permissions(вызывает себя, получае)
        if request.method in permissions.SAFE_METHODS: # если метод безопасен(принадлежит к чтению)
            return True #возвращаем его

        return bool(request.user and request.user.is_staff) # проверка что пользователь администратор
        
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj): #делаем разрешение на уровне объекта
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user == request.user # если пользов. из БД = пользователю который отправил запрос
                
