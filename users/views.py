from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

class RegisterAPIs(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user)
        print(token.key)
        return Response(
            {
                "messega" : "User created successfully.",
                "token" : token.key,
              }
        )
        # if serializer.is_valid() :
        #     user = serializer.save()
        #     token = Token.objects.create(user=user)
        #     print(token.key)
        #     return Response(
        #         {
        #             "messega" : "User created successfully.",
        #             "token" : token.key,
        #         }
        #     )
        # return Response(
        #         {
        #             "messega" : "Invalid Data. Try again!",
        #         }
        # )
