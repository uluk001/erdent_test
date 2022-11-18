from rest_framework import serializers
from apps.enroll.models import Enroll


class EnrollSerializers(serializers.ModelSerializer):
    class Meta:
        model=Enroll
        fields='__all__'
        read_only_fields=('patient',)

    
class EnrollListSerializers(serializers.ModelSerializer):
    class Meta:
        model=Enroll
        fields='__all__' 

        