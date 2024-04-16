from django.db import models
from django.contrib.auth.models import AbstractUser

HUMO , UZCARD , VISA = 'uzcard','humo','visa'


class User(AbstractUser):
    photo = models.ImageField(upload_to='users_photo/' , default='users_photo/default.png')
    phone_number = models.CharField(max_length=13, blank=True, null=True, unique=True)

    def __str__(self):
        return f"{self.username}"


class Card(models.Model):
    CARD_TYPE_CHOICES = (
        (HUMO, 'HUMO'),
        (UZCARD, 'UZCARD'),
        (VISA, 'VISA'),
    )

    card_number = models.CharField(max_length=16,unique=True,db_index=True)
    valid_time = models.CharField(max_length=40)
    card_type = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='cards')


    def __str__(self):
        return f"{self.name} : {self.card_number}"
