from rest_framework import serializers
from .models import *


class studserializer(serializers.ModelSerializer):
    class Meta:
        model=studinfo
        fields='__all__'