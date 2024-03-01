from rest_framework import serializers

from src.products import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ('author', 'name', 'start_date', 'cost',)
