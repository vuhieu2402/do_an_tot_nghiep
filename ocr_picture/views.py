from django.shortcuts import render

# Create your views here.

def ocr_picture_view(request):
    return render(request, 'ocr_picture/ocr_picture.html')
