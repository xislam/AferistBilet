from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


GENDER = (('Женщина', 'Женщина'),
          ('Мусчина', 'Мусчина'),)

USER_STATUS = (('Администратор', 'Администратор'), ('Пользователь', 'Пользователь'), ('Сотрудник', 'Сотрудник'))


class User(AbstractBaseUser, PermissionsMixin):
    inn_id = models.CharField(max_length=12, verbose_name='ИНН')
    fio = models.CharField(max_length=225, verbose_name='ФИО')
    gender = models.CharField(max_length=50, verbose_name='Пол', choices=GENDER)
    phone_number = PhoneNumberField(verbose_name='ТЕЛЕФОН', null=False, blank=False, unique=True)
    email = models.EmailField(verbose_name='Адрес электронной почты', unique=True)
    status = models.CharField(verbose_name='Статус пользователя', max_length=50, choices=USER_STATUS,
                              default='Пользователь')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    def __str__(self):
        return self.fio

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fio']

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'

