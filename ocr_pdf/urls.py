from django.urls import path
from .views import ocr_pdf_view

urlpatterns = [
    path('ocr-pdf/', ocr_pdf_view, name='ocr_pdf_view'),  # This is the URL for the OCR view. Replace 'ocr_pdf_view' with your view function name.
]