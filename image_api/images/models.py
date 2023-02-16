from django.db import models
from users.models import UserProfile
from PIL import Image as PILImage


# class Image(models.Model):
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='images/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)
#     image_basic = models.ImageField(upload_to='images/')
#     image_premium = models.ImageField(upload_to='images/')
#
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#
#         img = PILImage.open(self.image.path)
#         output_size_basic = (200, 200)
#         img.thumbnail(output_size_basic)
#         img.save(self.image_basic.path)
#
#
#         output_size_premium = (400, 400)
#         img = PILImage.open(self.image.path)
#         img.thumbnail(output_size_premium)
#         img.save(self.image_premium.path)

    # def __str__(self):
    #     return f"{self.image}"

class Image(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.image}"

#
# class ImageBasic(models.Model):
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     image_basic = models.ImageField(upload_to='images/')
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#
#         img = Image.open(self.image.path)
#
#
#         output_size = (200,200)
#         img.thumbnail(output_size)
#         img.save(self.image.path)
#     def __str__(self):
#         return f"{self.image}"
#
#
# class ImagePremium(models.Model):
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     image_premium = models.ImageField(upload_to='images/')
#
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#
#         img = Image.open(self.image.path)
#
#         output_size = (400, 400)
#         img.thumbnail(output_size)
#         img.save(self.image.path)
#
#     def __str__(self):
#         return f"{self.image}"

