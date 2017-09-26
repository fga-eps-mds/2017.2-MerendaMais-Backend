from counselor.models import Counselor
from rest_framework import viewsets
from .serializers import CounselorSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


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
