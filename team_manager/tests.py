from django.test import TestCase
from django.core.exceptions import ValidationError
from .validators import validate_phone_number
from .models import Member
from .forms import AddForm


class ValidatorTests(TestCase):
    def test_validate_phone_number_pass(self):
        """Test valid phone numbers"""
        num1 = "1234567891"
        num2 = "123.456.7891"
        num3 = "123 456 7891"
        num4 = "123-456-7891"
        self.assertIsNone(validate_phone_number(num1))
        self.assertIsNone(validate_phone_number(num2))
        self.assertIsNone(validate_phone_number(num3))
        self.assertIsNone(validate_phone_number(num4))

    def test_validate_phone_number_fail(self):
        """Test invalid phone numbers"""
        num1 = "1234567891a"
        num2 = "abc"
        num3 = "12"
        self.assertRaises(
            ValidationError,
            validate_phone_number,
            num1,
        )
        self.assertRaises(
            ValidationError,
            validate_phone_number,
            num2,
        )
        self.assertRaises(
            ValidationError,
            validate_phone_number,
            num3,
        )


class MemberModelTests(TestCase):
    def test_create_member_pass(self):
        """Test creating a member"""
        first_name = "test"
        last_name = "user"
        email = "test@email.com"
        phone = "1234567890"
        admin = "A"

        member = Member.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            admin=admin,
        )
        member.save()

        self.assertEqual(member.first_name, first_name)
        self.assertEqual(member.last_name, last_name)
        self.assertEqual(member.email, email)
        self.assertEqual(member.phone, phone)
        self.assertEqual(member.admin, admin)


class FormTests(TestCase):
    def test_clean_phone(self):
        """Test cleaning phone numbers"""
        res = "1234567890"
        form = AddForm()

        form.phone = "123 456-7890"
        self.assertEqual(form.clean_phone(), res)

        form.phone = "+123456.7890"
        self.assertEqual(form.clean_phone(), res)

        form.phone = "1234567890"
        self.assertEqual(form.clean_phone(), res)
