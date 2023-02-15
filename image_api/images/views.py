
from rest_framework import generics
from images.models import Image
from images.serializers import ImageSerializer
from rest_framework.permissions import IsAuthenticated




class ImageList(generics.ListAPIView):
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        user_profile = user.userprofile
        return Image.objects.filter(user=user_profile)

class ImageCreate(generics.CreateAPIView):
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]