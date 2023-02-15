from rest_framework import serializers
from images.models import Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

# class ImageBasic(serializers.ModelSerializer):
#     class Meta:
#         model = ImageBasic
#         fields = '__all__'
#
#
# class ImagePremium(serializers.ModelSerializer):
#     class Meta:
#         model = ImagePremium
#         fields = '__all__'
