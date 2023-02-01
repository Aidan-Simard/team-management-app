from django.core.exceptions import ValidationError


def validate_phone_number(number) -> None:
    """
    Helper function to validate phone numbers.
    Allows phone numbers with no spaces, or separated by spaces, periods, or hyphens.
    """
    valid_non_numeric = (" ", ".", "-")
    for num in number:
        if num not in valid_non_numeric and not num.isdigit():
            raise ValidationError(f'"{num}" is not a valid phone number character.')
