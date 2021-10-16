from rest_framework import serializers
from .models import Home


class HomeSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ['id', 'name', 'phone_number']