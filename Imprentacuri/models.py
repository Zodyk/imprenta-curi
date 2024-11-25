"""from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, password=None):

        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        if not username:
            raise ValueError('El usuario debe tener un nombre de usuario')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):

        user = self.create_user(email, username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username"""