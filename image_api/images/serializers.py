from rest_framework import serializers
from images.models import Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image', 'thumbnail_200', 'thumbnail_400', 'original_image', 'expiring_url']