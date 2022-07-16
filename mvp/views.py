from rest_framework import decorators, response, status, permissions
from django.template.loader import render_to_string
from django.core.mail import send_mail
# Create your views here.


@decorators.api_view(['POST'])
@decorators.permission_classes((permissions.AllowAny,))
def send_prelaunch_email(request):
    """
    Send a prelaunch email to the user.
    """
    request_body = request.data

    rendered = render_to_string(
        'mvp/prelaunch.html', {'first_name': request_body['firstname']})
    send_mail(
        'Welome to LAGBAJA MOBILE',
        rendered,
        'mide@lagbajamobile.com',
        [request_body['email'], "lagbajamobile@gmail.com"]

    )
    return response.Response({"success": True, 'message': f'Email successfully sent to {request_body["firstname"]}'}, status=status.HTTP_200_OK)
