from django.db import models


class DentalServicesCategory(models.Model):
    title=models.CharField(max_length=255)

    def __str__(self):
        return self.title


class DentalServicesList(models.Model):
    category=models.ForeignKey(DentalServicesCategory,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    price=models.PositiveIntegerField()

    def __str__(self) -> str:
        return f'{self.title}:{self.price}'