from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager

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
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('username', '')

        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser, UUIDModel):
    username = models.CharField(max_length=50, validators=[
                                CustomValidator.alphanumeric])
    email = models.EmailField(_('email address'), unique=True)

    first_name = None
    last_name = None

    fav_recipes = models.ManyToManyField(Recipe, blank=True)
    credit_card = models.CharField(max_length=16, default='', validators=[
                                   CustomValidator.creadit_card])

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class ShippingAddress(UUIDModel, TimeStampedModel):
    class Province(models.TextChoices):
        AB = 'AB', _('AB')
        BC = 'BC', _('BC')
        MB = 'MB', _('MB')
        NB = 'NB', _('NB')
        NS = 'NS', _('NS')
        NL = 'NL', _('NL')
        ON = 'ON', _('ON')
        PE = 'PE', _('PE')
        QC = 'QC', _('QC')
        SK = 'SK', _('SK')

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='shipping_address')

    full_name = models.CharField(max_length=50, validators=[
                                 CustomValidator.alphanumeric])
    phone_number = models.CharField(max_length=10, validators=[
                                    CustomValidator.phone_number])
    email = models.EmailField()

    address = models.CharField(max_length=50, default="", validators=[
        CustomValidator.alphanumeric])
    province = models.CharField(max_length=2, choices=Province.choices)
    postal_code = models.CharField(max_length=6, default='', validators=[
                                   CustomValidator.postal_code])

    def __str__(self):
        return self.user.username + ' address'
