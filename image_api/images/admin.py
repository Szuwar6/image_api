from django.contrib import admin

from images.models import Image
from users.models import UserProfile

admin.site.register(Image)
admin.site.register(UserProfile)
