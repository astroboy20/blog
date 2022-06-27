from rest_framework import generics, status, response, permissions
from . import serializers
from utils.custom_exception_handler import get_response
# Create your views here.


class UserCreateView(generics.GenericAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(get_response(message="User Created Successfully", result=serializer.data, success=True, status=status.HTTP_201_CREATED), status=status.HTTP_201_CREATED)
        return response.Response(get_response(message="Input Validation Error", errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST), status=status.TTP_400_BAD_REQUEST)
