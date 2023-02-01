from django.db import models


class Member(models.Model):
    """
    Model for storing team member information.
    Using automatic primary keys.
    """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    admin = models.CharField(
        max_length=1,
        choices=[
            ("R", "Regular - Can't delete members"),
            ("A", "Admin - Can delete members"),
        ],
    )
