from django.urls import path
from django.http import JsonResponse
from django.db import connection

def health(_request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        cursor.fetchone()
    return JsonResponse({"status":"ok","database":"postgresql"})

def message(_request):
    return JsonResponse({"message":"02-react-django-postgres is working"})

urlpatterns = [
    path("health", health),
    path("api/message", message),
]
