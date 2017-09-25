# Local Django.
from counselor.models import Counselor
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class CounselorSerializer(serializers.HyperlinkedModelSerializer):
    cpf = serializers.CharField(
        max_length=11,
        validators=[UniqueValidator(queryset=Counselor.objects.all())]
    )

    class Meta:
        model = Counselor
        fields = ('__all__')

        extra_kwargs = {
          'password': {'write_only': True}
        }

    def create(self, validated_data):
        counselor = Counselor.objects.create_user(**validated_data)
        return counselor
