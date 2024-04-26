from rest_framework import serializers
from .models import Batsman

class batsmanserializer(serializers.ModelSerializer):
    class Meta:
        model=Batsman
        fields="__all__"
