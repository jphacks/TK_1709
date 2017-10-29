from rest_framework import serializers

from .models import Item


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('id', 'name', 'description', 'image_url', 'price',
                  'deadline', 'created_at', 'status', 'username', 'category1', 'category2', 'category3', 'category4', 'category5')
