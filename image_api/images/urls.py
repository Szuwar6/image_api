from django.urls import path
from images.views import ImageList, ImageCreate


urlpatterns = [
    path('images/', ImageList.as_view(), name='list_images'),
    path('create/', ImageCreate.as_view(), name='create'),

]