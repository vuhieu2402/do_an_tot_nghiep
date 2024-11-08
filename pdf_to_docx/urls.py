from django.urls import path
from .views import convert_pdf_to_docx_view, result_page_view, download_docx_view

urlpatterns = [
    path('convert-pdf2docx/', convert_pdf_to_docx_view, name='convert_pdf2docx'),
    path('result-docx/', result_page_view, name='result_page'),
    path('download/', download_docx_view, name='download_docx'),
]
