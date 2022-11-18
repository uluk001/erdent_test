from rest_framework import serializers
from apps.medical_card.models import MedicalCards


class MedCardsCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model=MedicalCards
        fields=['id','patient', 'mrt', 'сonclusion', 'service' ,'total_price' ,'is_done']
        read_only_fields=('doctor',)
    
    def create(self, validated_data):
        service=validated_data['service']
        total=0
        for i in service:
            total+=i.price
        validated_data['total_price']=total    
        return super().create(validated_data)

    def update(self, instance, validated_data):
        service=validated_data['service']
        total=0
        for i in service:
            total+=i.price
        validated_data['total_price']=total   
        return super().update(instance, validated_data)


class CashierMedicalCardsPriceSerializers(serializers.ModelSerializer):
    class Meta:
        model=MedicalCards
        fields=['id','doctor', 'patient','service' ,'total_price','is_payed' ,'is_done']


class CashierMedicalCardsIsPayedSerializers(serializers.ModelSerializer):
    class Meta:
        model=MedicalCards
        fields=['is_payed']


class WeekActivitySerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = MedicalCards
        read_only_fields = ('doctor',)
        fields = (
            'id',
            'doctor',  
            'patient',
            'service',
            'mrt',
            'сonclusion',
            'data',
            'total_price',
            'is_done',
            'is_payed',
        )