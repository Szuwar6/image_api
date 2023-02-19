import os
from rest_framework import generics, status
from images.models import Image
from images.serializers import ImageSerializer

from rest_framework.permissions import IsAuthenticated
from PIL import Image as PILImage

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


# class ImageCreate(generics.CreateAPIView):
#     serializer_class = ImageSerializer
#     permission_classes = [IsAuthenticated]
#
#     def perform_create(self, serializer):
#         user = self.request.user
#         user_profile = user.userprofile
#         user_plan = user_profile.plan
#
#         if user_plan == Plan.ENTERPRISE:
#             serializer.save(user=user_profile)
#
#             image_file = PILImage.open(serializer.instance.image.path)
#
#             output_size = (200, 200)
#             image_200 = image_file.resize(output_size)
#             image_200_path = serializer.instance.image.path.replace('.', '_200.')
#             image_200.save(image_200_path)
#
#             output_size = (400, 400)
#             image_400 = image_file.resize(output_size)
#             image_400_path = serializer.instance.image.path.replace('.', '_400.')
#             image_400.save(image_400_path)
#
#         elif user_plan == Plan.PREMIUM:
#             serializer.save(user=user_profile)
#
#             image_file = PILImage.open(serializer.instance.image.path)
#
#             output_size = (200, 200)
#             image_200 = image_file.resize(output_size)
#             image_200_path = serializer.instance.image.path.replace('.', '_200.')
#             image_200.save(image_200_path)
#
#             output_size = (400, 400)
#             image_400 = image_file.resize(output_size)
#             image_400_path = serializer.instance.image.path.replace('.', '_400.')
#             image_400.save(image_400_path)
#
#         elif user_plan == Plan.BASIC:
#             serializer.save(user=user_profile)
#
#             image_file = PILImage.open(serializer.instance.image.path)
#
#             output_size = (200, 200)
#             image_200 = image_file.resize(output_size)
#             image_200_path = serializer.instance.image.path.replace('.', '_200.')
#             image_200.save(image_200_path)
#
#         else:
#             return Response({"error": "Nieprawidłowy plan"}, status=400)

class ImageCreate(generics.CreateAPIView):
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

    def create_image_for_enterprise(self, serializer):
        serializer.save(user=self.request.user.userprofile)
        image_file = PILImage.open(serializer.instance.image.path)
        output_size = (200, 200)
        image_200 = image_file.resize(output_size)
        image_200_path = serializer.instance.image.path.replace('.', '_200.')
        image_200.save(image_200_path)
        serializer.instance.image_200 = image_200_path
        output_size = (400, 400)
        image_400 = image_file.resize(output_size)
        image_400_path = serializer.instance.image.path.replace('.', '_400.')
        image_400.save(image_400_path)
        serializer.instance.image_400 = image_400_path
        serializer.save(image_200=image_200_path, image_400=image_400_path)

    def create_image_for_premium(self, serializer):
        serializer.save(user=self.request.user.userprofile)
        image_file = PILImage.open(serializer.instance.image.path)
        output_size = (200, 200)
        image_200 = image_file.resize(output_size)
        image_200_path = serializer.instance.image.path.replace('.', '_200.')
        image_200.save(image_200_path)
        serializer.instance.image_200 = image_200_path
        output_size = (400, 400)
        image_400 = image_file.resize(output_size)
        image_400_path = serializer.instance.image.path.replace('.', '_400.')
        image_400.save(image_400_path)
        serializer.instance.image_400 = image_400_path
        serializer.save()

    def create_image_for_basic(self, serializer):
        serializer.save(user=self.request.user.userprofile)
        image_file = PILImage.open(serializer.instance.image.path)
        output_size = (200, 200)
        image_200 = image_file.resize(output_size)
        image_200_path = serializer.instance.image.path.replace('.', '_200.')
        image_200.save(image_200_path)
        serializer.instance.image_200 = image_200_path
        os.remove(serializer.instance.image.path)
        serializer.save()

    def perform_create(self, serializer):
        user = self.request.user
        user_profile = user.userprofile
        user_plan = user_profile.plan

        if user_plan == Plan.ENTERPRISE:
            self.create_image_for_enterprise(serializer)

        elif user_plan == Plan.PREMIUM:
            self.create_image_for_premium(serializer)

        elif user_plan == Plan.BASIC:
            self.create_image_for_basic(serializer)

        else:
            return Response({"error": "Nieprawidłowy plan"}, status=400)
