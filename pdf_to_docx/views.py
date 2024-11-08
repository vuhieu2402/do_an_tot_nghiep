import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PDFUploadForm
from pdf2docx import Converter
import tempfile
import aspose.words as aw




def convert_pdf_to_docx_view(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = request.FILES['pdf_file']
            original_filename = pdf_file.name.rsplit('.', 1)[0]  # Lấy tên file gốc không bao gồm phần mở rộng

            # Lưu file PDF vào một file tạm thời
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
                for chunk in pdf_file.chunks():
                    temp_pdf.write(chunk)
                pdf_path = temp_pdf.name

            # Đường dẫn lưu file .docx sau khi chuyển đổi (sử dụng tên gốc)
            docx_path = os.path.join(tempfile.gettempdir(), f"{original_filename}.docx")

            try:
                # Chuyển đổi PDF sang DOCX bằng pdf2docx để lưu file tải về
                cv = Converter(pdf_path)
                cv.convert(docx_path, start=0, end=None)
                cv.close()

                # Lưu đường dẫn file DOCX để dùng cho việc tải về sau này
                request.session['converted_docx_path'] = docx_path

                # Sử dụng Aspose.Words để chuyển đổi PDF sang HTML cho hiển thị trên trang
                doc = aw.Document(pdf_path)
                html_path = os.path.join(tempfile.gettempdir(), f"{original_filename}.html")
                save_options = aw.saving.HtmlSaveOptions()
                save_options.pretty_format = True
                save_options.export_fonts_as_base64 = True  # Nhúng font để giữ định dạng gốc
                doc.save(html_path, save_options)

                # Đọc nội dung HTML để hiển thị trong template
                with open(html_path, 'r', encoding='utf-8') as file:
                    docx_html = file.read()

                # Thêm CSS tùy chỉnh để làm đẹp hiển thị và giữ định dạng gốc
                custom_css = """
                <style>
                    body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }
                    .docx-content { width: 100%; max-width: 900px; margin: auto; padding: 20px; border: 1px solid #ccc; background-color: #f9f9f9; border-radius: 8px; }
                    table { width: 100%; border-collapse: collapse; margin: 20px 0; }
                    th, td { border: 1px solid #ddd; padding: 8px; }
                    th { background-color: #f2f2f2; }
                    p { margin-bottom: 15px; }
                    img { max-width: 100%; height: auto; }
                </style>
                """
                docx_html = custom_css + f"<div class='docx-content'>{docx_html}</div>"

                request.session['docx_html'] = docx_html

            finally:
                # Xóa file PDF tạm thời sau khi xử lý
                os.remove(pdf_path)

            # Redirect đến trang kết quả
            return redirect('result_page')
    else:
        form = PDFUploadForm()

    return render(request, 'pdf_to_docx/pdf2docx.html', {'form': form})

def download_docx_view(request):
    docx_path = request.session.get('converted_docx_path')
    if not docx_path or not os.path.exists(docx_path):
        return HttpResponse("Không tìm thấy file để tải xuống. Vui lòng thử lại.")

    with open(docx_path, 'rb') as docx_file:
        response = HttpResponse(
            docx_file.read(),
            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(docx_path)}"'
        return response






def result_page_view(request):
    docx_html = request.session.get('docx_html')
    if not docx_html:
        return HttpResponse("Không tìm thấy kết quả. Vui lòng thử lại.")

    return render(request, 'pdf_to_docx/result.html', {'docx_html': docx_html})







# def convert_pdf_to_docx_view(request):
#     if request.method == 'POST':
#         form = PDFUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             pdf_file = request.FILES['pdf_file']
#             original_filename = pdf_file.name.rsplit('.', 1)[0]  # Lấy tên file gốc không bao gồm phần mở rộng
#
#             # Lưu file PDF vào một file tạm thời
#             with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
#                 for chunk in pdf_file.chunks():
#                     temp_pdf.write(chunk)
#                 pdf_path = temp_pdf.name
#
#             # Đường dẫn lưu file .docx sau khi chuyển đổi (sử dụng tên gốc)
#             docx_path = os.path.join(tempfile.gettempdir(), f"{original_filename}.docx")
#
#             try:
#                 # Sử dụng Aspose.Words để chuyển đổi PDF sang DOCX
#                 doc = aw.Document(pdf_path)
#                 doc.save(docx_path)
#
#                 # Chuyển đổi DOCX sang HTML bằng Aspose.Words
#                 html_path = os.path.join(tempfile.gettempdir(), f"{original_filename}.html")
#                 save_options = aw.saving.HtmlSaveOptions()
#                 save_options.pretty_format = True
#                 save_options.export_fonts_as_base64 = True  # Nhúng font để giữ định dạng gốc
#
#                 # Lưu tài liệu thành file HTML
#                 doc = aw.Document(docx_path)
#                 doc.save(html_path, save_options)
#
#                 # Đọc nội dung HTML
#                 with open(html_path, 'r', encoding='utf-8') as file:
#                     docx_html = file.read()
#
#                 # Thêm CSS tùy chỉnh để làm đẹp hiển thị và giữ định dạng gốc
#                 custom_css = """
#                 <style>
#                     body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }
#                     .docx-content { width: 100%; max-width: 900px; margin: auto; padding: 20px; border: 1px solid #ccc; background-color: #f9f9f9; border-radius: 8px; }
#                     table { width: 100%; border-collapse: collapse; margin: 20px 0; }
#                     th, td { border: 1px solid #ddd; padding: 8px; }
#                     th { background-color: #f2f2f2; }
#                     p { margin-bottom: 15px; }
#                     img { max-width: 100%; height: auto; }
#                 </style>
#                 """
#                 docx_html = custom_css + f"<div class='docx-content'>{docx_html}</div>"
#
#                 request.session['docx_html'] = docx_html
#                 request.session['converted_docx_path'] = docx_path  # Lưu đường dẫn .docx
#                 request.session['original_filename'] = original_filename  # Lưu tên gốc để sử dụng khi tải về
#
#             finally:
#                 # Xóa file PDF tạm thời
#                 os.remove(pdf_path)
#
#             # Redirect đến trang kết quả
#             return redirect('result_page')
#     else:
#         form = PDFUploadForm()
#
#     return render(request, 'pdf_to_docx/pdf2docx.html', {'form': form})
# def download_docx_view(request):
#     docx_path = request.session.get('converted_docx_path')
#     original_filename = request.session.get('original_filename', 'converted_document')
#
#     if not docx_path or not os.path.exists(docx_path):
#         return HttpResponse("Không tìm thấy file để tải xuống. Vui lòng thử lại.")
#
#     # Đổi tên file tải về với tên gốc và đuôi .docx
#     download_filename = f"{original_filename}.docx"
#
#     with open(docx_path, 'rb') as docx_file:
#         response = HttpResponse(docx_file.read(),
#                                 content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#         response['Content-Disposition'] = f'attachment; filename="{download_filename}"'
#         return response

