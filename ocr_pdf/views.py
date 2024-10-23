from django.shortcuts import render

# Create your views here.

def ocr_pdf_view(request):
    return render(request, 'ocr_pdf/ocr_pdf.html')