
from django.urls import path
from .views import  ocr_picture_view, convert_images


urlpatterns = [
    path('ocr-picture/', ocr_picture_view, name='ocr_picture'),  # URL to the OCR picture view
    path('convert/', convert_images, name='convert_images'),

]

