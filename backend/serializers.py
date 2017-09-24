# Local Django.
from counselor.models import Counselor
from rest_framework import serializers


class CounselorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Counselor
        fields = (
         'url',
         'cpf',
         'email',
         'phone',
         'name',
         'isPresident',
         'segment',
         'CAE_Type',
         'CAE'
        )
