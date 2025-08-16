from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils.translation import gettext_lazy as _



class CustomerUserManager(BaseUserManager):
    
    """A custom manager for CustomUser model that uses phone_number as the unique identifier.
    """
    def create_user(self,phone_number, password=None, **extra_fields):
        """
        Create User with the given phone_number and password
        
        """
        if not phone_number:
            raise ValueError(_("The phone_number must be provided."))
        user = self.model(phone_number=phone_number,**extra_fields) 
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self,phone_number, password=None, **extra_fields):
        """
        Create Superuser with the given phone_number and password

        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(phone_number, password, **extra_fields)



class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomerUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []  # additional fields for createsuperuser

    def __str__(self):
        return str(self.phone_number)
    