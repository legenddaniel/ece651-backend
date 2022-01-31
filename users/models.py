from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager

from model_utils.models import UUIDModel, TimeStampedModel

from recipes.models import Recipe
from project.validators import CustomValidator


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        return self.__create_user(email, password, **other_fields)

    def create_user(self, email, password, **other_fields):
        other_fields.setdefault("is_staff", False)
        other_fields.setdefault("is_superuser", False)

        return self.__create_user(email, password, **other_fields)

    def __create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))

        other_fields.setdefault('is_active', True)

        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser, UUIDModel):
    username = models.CharField(max_length=50, default='', validators=[
                                CustomValidator.alphanumeric])
    email = models.EmailField(_('email address'), unique=True)

    first_name = None
    last_name = None

    fav_recipes = models.ManyToManyField(Recipe)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class ShippingAddress(UUIDModel, TimeStampedModel):
    class Province(models.TextChoices):
        ON = 'ON', _('ON')
        # ...more

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=50, validators=[
                                 CustomValidator.alphanumeric])
    phone_number = models.CharField(max_length=10, validators=[
                                    CustomValidator.phone_number])
    email = models.EmailField()
    address1 = models.CharField(max_length=10, validators=[
                                CustomValidator.alphanumeric])
    address2 = models.CharField(max_length=10, default='', validators=[
                                CustomValidator.alphanumeric])
    province = models.CharField(max_length=2, choices=Province.choices)
