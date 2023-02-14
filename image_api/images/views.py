from rest_framework import viewsets
from .models import Image
from .serializers import ImageSerializer
from rest_framework import generics
from rest_framework import permissions
from images.models import Image

from .serializers import ImageSerializer
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer



class ImageUploadView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ImageSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ImageListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ImageSerializer

    def get_queryset(self):
        return Image.objects.filter(user=self.request.user)


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageListView(viewsets.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer