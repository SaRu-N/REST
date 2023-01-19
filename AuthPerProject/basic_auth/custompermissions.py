from rest_framework.authentication import BasicAuthentication


class MyPermission(BasicAuthentication):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        return False
    def has_object_permission(self,request,view,obj):
        if request.method == "GET":
            return True
        return False