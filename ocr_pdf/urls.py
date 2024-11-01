from django.urls import path
from .views import ocr_pdf_view, convert_pdf

urlpatterns = [
    path('ocr-pdf/', ocr_pdf_view, name='ocr_pdf_view'),
    path('convert-pdf/', convert_pdf, name='convert_pdf'),
]
