from rest_framework import serializers
from .models import ModelAla


class AlaSerializers(serializers.ModelSerializer):
    class Meta:
        model = ModelAla
        fields = '__all__'