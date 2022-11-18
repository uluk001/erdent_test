from django.db import models
from django.contrib.auth.models import AbstractUser


class Branch(models.Model):
    # Филиалы Эрдента
    address=models.CharField(max_length=255)

    def __str__(self):
        return self.address


class Schedule(models.Model):
    # График работы
    from_time =models.TimeField()
    to_time=models.TimeField()

    def __str__(self):
        return f'from time: {self.from_time} to:{self.to_time}'


class User(AbstractUser):
    # Все пользователи
    username = models.CharField(max_length=255, unique=True)
    email=models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=13,blank=True, null=True)
    birth_date=models.DateField( blank=True, null=True)
    photo=models.ImageField(upload_to='avatars/',null=True,blank=True)

    # for doctors
    specialization=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True,blank=True)

    # for admin
    is_operator = models.BooleanField(default=False)
    is_doctor=models.BooleanField(default=False)
    schedule=models.ForeignKey(Schedule,on_delete=models.CASCADE, null=True,blank=True)
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE, null=True,blank=True)

    REQUIRED_FIELDS=['phone_number']

    def __str__(self):
        return f"{self.username}"

    class Meta:
        ordering = ("id",)
