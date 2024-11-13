
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('ocr_picture.urls')),
    path('', include('ocr_pdf.urls')),
    path('', include('pdf_to_docx.urls')),
    path('', include('translate.urls')),
]
