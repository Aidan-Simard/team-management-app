from django.core.exceptions import ValidationError
import re

INVALID_NUM = "Enter a valid phone number."


def validate_phone_number(number) -> None:
    """
    Helper function to validate phone numbers.

    Regex from: https://www.oreilly.com/library/view/regular-expressions-cookbook/9780596802837/ch04s02.html
    """

    if re.match("^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$", number) == None:
        raise ValidationError(INVALID_NUM)
