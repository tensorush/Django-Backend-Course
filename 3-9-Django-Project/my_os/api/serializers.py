from rest_framework import serializers

from .models import System, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class SystemSerializer(serializers.ModelSerializer):
    categories = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = System
        fields = ['id', 'name', 'categories', 'logo']
