from rest_framework import decorators, permissions, response, status

# Create your views here.


@decorators.api_view(['GET'])
@decorators.permission_classes((permissions.AllowAny,))
def home(request):

    return response.Response({'message': 'Hello, World!'}, status=status.HTTP_200_OK)
