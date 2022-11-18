import datetime

from rest_framework import generics
from rest_framework.response import Response
from apps.enroll.models import Enroll
from apps.enroll.serializers import EnrollSerializers,EnrollListSerializers
from apps.user.permissions import IsOperator,IsOwner,IsDoctors
from apps.user.models import Schedule,User
from apps.user.serializers import DoctorProfileSerializerList


class EnrollCreateApiView(generics.CreateAPIView):
    queryset=Enroll.objects.all()
    serializer_class=EnrollSerializers

    def perform_create(self, serializer):
        return serializer.save(patient=self.request.user)
    

class DoctorsTime(generics.RetrieveAPIView):
    serializer_class = DoctorProfileSerializerList
    permission_classes = [IsOwner or IsDoctors]

    def get(self, request, *args, **kwargs):
        doctor = User.objects.get(id=self.kwargs['pk'], is_doctor=True)
        if Schedule.objects.all():
            schedules = Schedule.objects.latest('id')
            time1 = schedules.from_time
            time2 = schedules.to_time

            t1 = datetime.datetime.strptime(str(time1),'%H:%M:%S').time()
            t2 = datetime.datetime.strptime(str(time2),'%H:%M:%S').time()
            h1, m1, s1 = t1.hour, t1.minute, t1.second
            h2, m2, s2 = t2.hour, t2.minute, t2.second
            total_hour = h2-h1
            minute = m2-m1
            all_times = []
            dates = []
            total_res = {}
            today = datetime.date.today()
            t = h1
            for h in range(total_hour):
                if t<10:
                    all_times.append(f'0{t}:00:00')
                else:
                    all_times.append(f'{t}:00:00')
                t+=1
            for i in Enroll.objects.filter(doctor=self.kwargs['pk']):
                for d in range(7):
                    res=today+datetime.timedelta(days=d)
                    # total_res[d]=res
                    dates.append(res)
                    total_res[f'free times {res}']=all_times
                    if i.date == res:
                        if str(i.from_time) in all_times:
                            all_times.remove(str(i.from_time))
            return Response({'doctor':doctor.username,'total ':total_res})
        return Response({'doctor':doctor.username,'all free times':0})


class DoctorsPatientForTodayApiView(generics.ListAPIView):
    serializer_class=EnrollListSerializers
    permission_classes=[IsDoctors]

    def get(self, request, *args, **kwargs):
        today = datetime.date.today() # сегодняшняя дата
        all_patients = []
        todays_patients = [] # Что бы сохранить сегодняшних клиентов
        tomorrows_patients = [] # Что бы сохранить завтрашних клиентов
        tomorrow = today + datetime.timedelta(days=2) # Берём завтрашний день
        enrolls = Enroll.objects.filter(doctor=self.request.user)
        all_enrolls = Enroll.objects.all()
        for i in enrolls:
            # Условие на сегодняшние записи
            if i.date == today and i.from_time > datetime.datetime.now().time():
                todays_patients.append(f"id:{i.id} - username: {i.patient.username} - date: {i.date} - at: {i.from_time}")
            # Условие на завтрашние записи
            if i.date > today and i.date < tomorrow:
                tomorrows_patients.append(f"id:{i.id} - username: {i.patient.username} - date: {i.date} - at: {i.from_time}")
        for i in all_enrolls:
        # Условие на все нынешние и будущие записи
            if i.date >= today:
                all_patients.append(f"id:{i.id} - username: {i.patient.username} - date: {i.date} - at: {i.from_time}")
            
        return Response({'Today\'s enrolls':todays_patients, 'Tomorrow\'s enrolls':tomorrows_patients, 'All enrolls':all_patients})


class OperatorsApiView(generics.ListAPIView):
    permission_classes=(IsOperator,)
    serializer_class=EnrollSerializers

    def get_queryset(self):
        operator=self.request.user.branch
        return Enroll.objects.filter(doctor__branch=operator)


class OperatorDeleteApiView(generics.RetrieveDestroyAPIView):
    permission_classes=[IsOperator|IsOwner]
    serializer_class=EnrollSerializers

    def get_queryset(self):
        operator=self.request.user.branch
        return Enroll.objects.filter(doctor__branch=operator)
