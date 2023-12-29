from rest_framework import serializers
from .models import Tag

class Userserilizer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields='__all__'