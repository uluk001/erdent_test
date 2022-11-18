from django.db import models
from apps.user.models import User


class Enroll(models.Model):
    patient=models.ForeignKey(User,on_delete=models.CASCADE,related_name='patient')
    doctor=models.ForeignKey(User,on_delete=models.CASCADE)
    from_time=models.TimeField()
    date=models.DateField()

    def __str__(self):
        return f'Пациент: {self.patient.username} Доктор: {self.doctor.username}'

    class Meta:
        unique_together = ('doctor', 'from_time','date',)