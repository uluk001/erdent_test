from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(obj == request.user)


class IsOperator(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_operator==True:
            return True  
        else:
            return False


class IsDoctors(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_doctor==True:
            return True  
        else:
            return False    
