from django import forms
from .validators import validate_phone_number


class AddForm(forms.Form):
    """
    Form for getting team member information.
    """

    first_name = forms.CharField(
        label="",
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "form-control",
            }
        ),
    )

    last_name = forms.CharField(
        label="",
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "class": "form-control",
            }
        ),
    )

    email = forms.EmailField(
        label="",
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control",
            }
        ),
    )

    phone = forms.CharField(
        label="",
        max_length=50,
        required=True,
        validators=[validate_phone_number],
        widget=forms.TextInput(
            attrs={
                "placeholder": "Phone Number",
                "class": "form-control",
            }
        ),
    )

    admin = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=[
            ("R", "Regular - Can't delete members"),
            ("A", "Admin - Can delete members"),
        ],
        initial="R",
    )
