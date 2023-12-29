from rest_framework import serializers
from .models import UserApp

class Userserilizer(serializers.ModelSerializer):
    class Meta:
        model=UserApp
        fields='__all__'