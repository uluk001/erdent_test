from rest_framework import serializers

from apps.user.models import *


class BranchSerializerList(serializers.ModelSerializer):
     # Филиалы Эрдента
    class Meta:
        model = Branch
        fields = '__all__'


class UserSerializerList(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (  
            "id",
            "username",
            "email",
            "phone_number",
            "birth_date",
            "photo",
            'password',
            )

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class DoctorProfileSerializerList(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "phone_number",
            "birth_date",
            "photo",
            "specialization",
            "description",
            'password',
            )


class AdminConfirmationSrializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "is_doctor",
            "is_operator",
            "branch",
            )
