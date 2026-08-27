from django.urls import path
from django.http import JsonResponse
from django.db import connection

def health(_request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        cursor.fetchone()
    return JsonResponse({"status":"ok","database":"mysql"})

def message(_request):
    return JsonResponse({"message":"08-vue-django-mysql is working"})

urlpatterns = [
    path("health", health),
    path("v1/message", message),
]
