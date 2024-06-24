from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models
from django.utils.crypto import get_random_string
from django.utils import timezone
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        """
        Creates and saves a User with the given phone number and password.
        """
        if not phone_number:
            raise ValueError("The phone number must be set")

        # Generate an OTP and set it in the user object
        otp = get_random_string(length=4, allowed_chars="0123456789")
        user = self.model(phone_number=phone_number, otp=otp, **extra_fields)
        user.set_password(password)  # Set the password using Django's built-in method
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given phone number and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        # Set the username to be the same as the phone number if it's not blank
        extra_fields.setdefault("username", phone_number)

        return self.create_user(phone_number, password, **extra_fields)


class Role(models.Model):
    name = models.CharField(unique=True, max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    phone_number = models.CharField(
        max_length=10,  # Phone numbers should be exactly 10 digits long
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^\d{10}$",  # Ensure that the phone number has exactly 10 digits
                message="Phone number must be exactly 10 digits long.",
            )
        ],
    )
    phone_number_verification = models.BooleanField(default=False, blank=True)
    email = models.EmailField(
         max_length=100,
         unique=True,
         blank=True,  # Allow empty email addresses if needed
         null=True,   # Allow null email addresses if needed
     )
    email_verification = models.BooleanField(default=False, null=True,blank=True)
    otp = models.IntegerField(null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    expiry_time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    objects = UserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []
    # Add any other custom fields or methods specific to your application
    is_anonymous = False

    def save(self, *args, **kwargs):
        # Automatically set the username to the phone_number before saving
        self.username = self.phone_number
        super().save(*args, **kwargs)

    def is_expired(self):
        return self.expiry_time < timezone.now()

    def __str__(self):
        return str(self.phone_number)
