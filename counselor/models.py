# Django.

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class CounselorManager(BaseUserManager):
    def create_user(
        self,
        cpf,
        email,
        phone,
        name,
        password,
        isPresident,
        segment,
        CAE_Type,
        CAE,
        **kwargs
    ):
        counselor = Counselor()

        counselor.email = self.normalize_email(email)
        counselor.phone = phone
        counselor.cpf = cpf
        counselor.name = name
        counselor.set_password(password)
        counselor.isPresident = isPresident
        counselor.segment = segment
        counselor.CAE_Type = CAE_Type
        counselor.CAE = CAE

        counselor.save(using=self.db)

        return counselor


class Counselor(AbstractBaseUser):
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50, primary_key=True)
    isPresident = models.BooleanField(default=False)
    segment = models.CharField(max_length=50)
    CAE_Type = models.CharField(max_length=50)
    CAE = models.CharField(max_length=50)

    objects = CounselorManager()

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = [
        'email',
        'phone',
        'name',
        'isPresident',
        'segment',
        'CAE_Type',
        'CAE',
        ]
