from django.urls import path
from .views import TokenApi, CarApi, UserApi

app_name="api"
urlpatterns = [
    path("auth", TokenApi.as_view()), 
    path("cars", CarApi.as_view()), 
    path("users", UserApi.as_view()), 
]
