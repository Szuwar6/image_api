import os

from rest_framework import generics
from images.models import Image
from images.serializers import ImageSerializer
from rest_framework.permissions import IsAuthenticated
from PIL import Image as PILImage
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from users.models import Plan


class ImageList(generics.ListAPIView):
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        user_profile = user.userprofile
        return Image.objects.filter(user=user_profile)

# class ImageCreate(generics.CreateAPIView):
#     serializer_class = ImageSerializer
#     permission_classes = [IsAuthenticated]
#
#
#
#     def image_create(self, serializer):
#
#         user = self.request.user
#         user_profile = user.userprofile
#         user_plan = user_profile.plan
#         if user_plan == "Enterprise":
#
#
#             # user = self.request.user
#             # user_profile = user.userprofile
#             # serializer.save(user=user_profile)
#
#             image_file = PILImage.open(serializer.instance.image.path)
#
#             output_size = (200, 200)
#             image_200 = image_file.resize(output_size)
#             image_200_path = serializer.instance.image.path.replace('.', '_200.')
#             image_200.save(image_200_path)
#
#
#             output_size = (400, 400)
#             image_400 = image_file.resize(output_size)
#             image_400_path = serializer.instance.image.path.replace('.', '_400.')
#             image_400.save(image_400_path)
#
#         else:
#             raise PermissionDenied(detail="Wrong plan")


class ImageCreate(generics.CreateAPIView):
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        user_profile = user.userprofile
        user_plan = user_profile.plan

        if user_plan == Plan.ENTERPRISE:
            serializer.save(user=user_profile)

            image_file = PILImage.open(serializer.instance.image.path)

            output_size = (200, 200)
            image_200 = image_file.resize(output_size)
            image_200_path = serializer.instance.image.path.replace('.', '_200.')
            image_200.save(image_200_path)

            output_size = (400, 400)
            image_400 = image_file.resize(output_size)
            image_400_path = serializer.instance.image.path.replace('.', '_400.')
            image_400.save(image_400_path)

        elif user_plan == Plan.PREMIUM:
            serializer.save(user=user_profile)

            image_file = PILImage.open(serializer.instance.image.path)

            output_size = (200, 200)
            image_200 = image_file.resize(output_size)
            image_200_path = serializer.instance.image.path.replace('.', '_200.')
            image_200.save(image_200_path)

            output_size = (400, 400)
            image_400 = image_file.resize(output_size)
            image_400_path = serializer.instance.image.path.replace('.', '_400.')
            image_400.save(image_400_path)

        elif user_plan == Plan.BASIC:
            serializer.save(user=user_profile)

            image_file = PILImage.open(serializer.instance.image.path)

            output_size = (200, 200)
            image_200 = image_file.resize(output_size)

            image_200_path = serializer.instance.image.path.replace('.', '_200.')
            image_200.save(image_200_path)
            os.remove(serializer.instance.image.path)


        else:
            return Response({"error": "Nieprawidłowy plan"}, status=400)