from django.http import response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime, timedelta
import jwt
from .models import Tokens, Cars, Users

# Create your views here.
class TokenApi(APIView):
    def post(self, request):
        user=Users.objects.filter(id = request.data["id"]).first().perfil
        info = {
            "expiration_date": str(datetime.now() + timedelta(seconds = 60)),
            "profile": user
        }
        token=jwt.encode(info, "secret", algorithm = "HS256")
        user=Users.objects.filter(id = request.data["id"]).first()
        token=Tokens.objects.create(token=token, user= user).pk
        return Response(
            {"pk":token},status=status.HTTP_200_OK
        )
    def get(self, request):
        token = Tokens.objects.filter(id = request.GET["id"]).first()
        #user=Users.objects.filter(id = token.user.pk).first().pk
        return Response(
            {"token":token.token, "pk": token.user.pk},status=status.HTTP_200_OK

        )
        
class CarApi(APIView):
    def post (self, request):
        token=jwt.decode(request.data["token"], "secret", algorithms = "HS256")
        if not "admin" in token["profile"]:
            return Response(
                status = status.HTTP_401_UNAUTHORIZED
            )
        request.data.pop("token")
        car = Cars.objects.create(**request.data).pk
        return Response(
            {"pk": car}, status=status.HTTP_201_CREATED
        )

    def get(self, request):
        car = Cars.objects.all().values()
        return Response(
            {"data":car}, status=status.HTTP_200_OK
        )
    def delete(self, request):
        token = Tokens.objects.filter(id = request.GET["id"]).first().delete()
        return Response(
            status=status.HTTP_200_OK
        )

class UserApi(APIView):
    def post (self, request):
        user = Users.objects.create(**request.data).pk
        return Response(
            {"pk":user}, status=status.HTTP_201_CREATED
        )
       
    def get(self, request):
        user = Users.objects.all().values()
        return Response(
            {"data":user}, status=status.HTTP_200_OK
        )