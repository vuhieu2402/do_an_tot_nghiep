from django.shortcuts import render, redirect
from .ocr import process_uploaded_pdf
# Create your views here.

def ocr_pdf_view(request):
    return render(request, 'ocr_pdf/ocr_pdf.html')


def convert_pdf(request):
    if request.method == 'POST' and request.FILES.get('pdf'):
        uploaded_pdf = request.FILES.get('pdf')

        # Gọi hàm OCR để xử lý PDF và lấy kết quả văn bản
        result_html = process_uploaded_pdf(uploaded_pdf)

        # Truyền kết quả OCR vào template
        context = {
            'result_html': result_html,
            'text': result_html,
        }
        return render(request, 'ocr_pdf/result.html', context)

    return redirect('ocr_picture')