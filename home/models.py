from django.db import models

# Create your models here.
class BaseUser(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    class Meta:
        abstract = True


class Users_info(BaseUser):
    pass


class Dog(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)


class Users(BaseUser):
    password = models.CharField(max_length=50)
