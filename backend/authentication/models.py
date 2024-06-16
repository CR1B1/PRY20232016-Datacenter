from django.db import models 
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.signals import pre_save
from django.dispatch import receiver

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", 512)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                "Superuser must have is_staff=True."
            )
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must have is_superuser=True."
            )

        return self._create_user(email, password, **extra_fields)
    
class UserArea(models.Model):
    area_name = models.CharField(max_length=150, null=True)
    def __str__(self):
        return f'{self.area_name}'    

class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    role = models.IntegerField(choices=((512,'Administrator'),(255, 'Manager'), (1, 'Empleado')), null=True)
    dni = models.IntegerField(null=True)
    profile_photo = models.ImageField(upload_to="images", null=True, default='images/default_image.jpg')
    user_area = models.ForeignKey(UserArea, related_name='user_area', null=True, blank=True, on_delete=models.SET_NULL)
    administrator = models.ForeignKey('self', related_name='administrator_user', null=True, on_delete=models.CASCADE)
    authorization = models.IntegerField(choices=((2,'Autorizado'),(1, 'Espera'), (0, 'No-autorizado')), null=True, default=0)
    change_password = models.BooleanField(default=False)
    company_logo = models.ImageField(upload_to="company_logo/", null=True, blank=True)
    showed_password_change_request = models.BooleanField(default=False)
    USERNAME_FIELD = "email" 
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    
@receiver(pre_save, sender=User)
def user_handler(sender, instance, *args, **kwargs):
    instance.email = instance.email.lower()