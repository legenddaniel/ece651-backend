from django.core.validators import RegexValidator


class CustomValidator:
    alphanumeric = RegexValidator(
        r'^[0-9a-zA-Z ]*$', 'Only alphanumeric characters and whitespaces are allowed.')
    phone_number = RegexValidator(
        r'^\d{10}$', 'Phone number must be entered in the format: 1234567890.')
    creadit_card = RegexValidator(
        r'^\d{16}$', 'Credit card number must be 16 digit numbers.')
