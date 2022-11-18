from django.db import models
from apps.user.models import User
from apps.dental.models import DentalServicesList


class MedicalCards(models.Model):
    # мед карты 
    patient=models.ForeignKey(User,on_delete=models.PROTECT,related_name='patients_card')
    doctor=models.ForeignKey(User,on_delete=models.PROTECT, related_name='doctor')
    service=models.ManyToManyField(DentalServicesList)
    mrt = models.ImageField(upload_to='mrt_images/', null=True, blank=True)
    сonclusion = models.TextField(null=True)
    data = models.DateField(auto_now_add=True)
    total_price = models.PositiveIntegerField(default=0)
    is_done = models.BooleanField(default=False)
    is_payed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.doctor}'


class CartArchive:
   pass