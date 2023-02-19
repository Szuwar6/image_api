from rest_framework import serializers
from images.models import Image

class ImageSerializer(serializers.ModelSerializer):
    image_200 = serializers.SerializerMethodField()
    image_400 = serializers.SerializerMethodField()

    def get_image_200(self, obj):
        return "http://127.0.0.1:8000" + obj.image.url

    def get_image_400(self, obj):
        return "http://127.0.0.1:8000" + obj.image.url
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




