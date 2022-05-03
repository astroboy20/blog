from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny
from . import serializers
from utils.custom_exception_handler import get_response
# Create your views here.


class UserCreateView(GenericAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(get_response(message="User Created Successfully", result=serializer.data, success=True, status=HTTP_201_CREATED), status=HTTP_201_CREATED)
        return Response(get_response(message="Input Validation Error", errors=serializer.errors, status=HTTP_400_BAD_REQUEST), status=HTTP_400_BAD_REQUEST)
