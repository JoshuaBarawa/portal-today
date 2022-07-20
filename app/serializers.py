from rest_framework import serializers
from .models import *


class ItemSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['image', 'name', 'description']


class ItemSerializerGET(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'image', 'name', 'description']
