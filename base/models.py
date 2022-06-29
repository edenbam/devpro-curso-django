from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, email, password):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email,password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password):
        pass


class User(AbstractBaseUser):
    email = models.EmailField(("email address"), unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
