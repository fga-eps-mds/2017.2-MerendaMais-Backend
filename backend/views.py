# Python
import requests
import json

# Django
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import detail_route
from django.http import HttpResponse

# Local Django
from . import constants
from .serializers import CounselorSerializer
from counselor.models import Counselor


class SchoolViewSet(viewsets.ModelViewSet):

    @detail_route(methods=['post'])
    @csrf_exempt
    def get_schools(self, request, *args, **kwargs):
        print(request.data)

        payload = {
                    'nome': request.data.get('name'),
                    'municipio': request.data.get('city')
                  }

        r = requests.get(constants.SCHOOL_ENDP, params=payload)

        # Converts the string response into json/python dict
        r = r.json()

        # Response variable which will be returned to React App.
        response = []

        # For each position in my response array, search each key.
        # If a key is name, append its value to our response.

        for each_element in r:
            response.append({'nome': each_element['nome']})

        # Convert list to Json.
        response = json.dumps(response)
        return HttpResponse(response)


class CounselorViewSet(viewsets.ModelViewSet):
    queryset = Counselor.objects.all()
    serializer_class = CounselorSerializer


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(
            request,
            *args,
            **kwargs)
        token = Token.objects.get(key=response.data['token'])
        counselor = Counselor.objects.all().get(id=token.user_id)
        return Response(
            {
                'token': token.key,
                'name': counselor.name,
                'cpf': counselor.cpf,
                'id': counselor.id
            }
        )
