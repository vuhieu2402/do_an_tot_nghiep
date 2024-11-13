from django.urls import path
from .views import  convert_and_translate_pdf_to_docx_view, download_translated_docx_view, result_view, convert_and_translate_docx_view

urlpatterns = [
    path('translate-pdf/', convert_and_translate_pdf_to_docx_view, name='translate_pdf2docx'),
    path('translate-docx/', convert_and_translate_docx_view, name='translate_docx'),
    path('result-trans/', result_view, name='result_trans'),
    path('download-translated/', download_translated_docx_view, name='download_translated_docx'),
]
