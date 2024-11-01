from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .ocr import process_uploaded_image


# Create your views here.

def ocr_picture_view(request):
    return render(request, 'ocr_picture/ocr_picture.html')


def convert_images(request):
    if request.method == 'POST' and request.FILES.getlist('images'):
        uploaded_files = request.FILES.getlist('images')

        # Gọi hàm OCR từ ocr.py và nhận kết quả văn bản OCR
        result_html = process_uploaded_image(uploaded_files)

        # In nội dung HTML để kiểm tra
        print(result_html)

        # Truyền kết quả OCR vào template
        context = {
            'result_html': result_html,  # HTML cho kết quả
            'text': result_html,  # Để sử dụng trong Quill editor
        }
        return render(request, 'ocr_picture/result.html', context)

    return redirect('ocr_picture')

# @csrf_exempt
# def download_docx(request):
#     if request.method == 'POST':
#         content = request.POST.get("content", "")
#
#         # Kiểm tra xem có nội dung không
#         if not content:
#             return HttpResponse("No content provided.", status=400)
#
#         # Sử dụng BeautifulSoup để xử lý HTML
#         soup = BeautifulSoup(content, "html.parser")
#
#         # Tạo một tài liệu mới
#         doc = Document()
#
#         # Thêm nội dung vào tài liệu
#         for element in soup.find_all():
#             if element.name == 'p':
#                 doc.add_paragraph(element.get_text())
#             elif element.name == 'table':
#                 rows = element.find_all('tr')
#                 if not rows:
#                     continue  # Nếu không có hàng nào, bỏ qua bảng
#
#                 num_cols = len(rows[0].find_all('td'))  # Số cột từ hàng đầu tiên
#                 table = doc.add_table(rows=len(rows), cols=num_cols)
#
#                 for i, row in enumerate(rows):
#                     cells = row.find_all('td')
#                     for j, cell in enumerate(cells):
#                         if j < num_cols:
#                             table.cell(i, j).text = cell.get_text()
#
#         # Đặt kiểu trả về
#         response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#         response['Content-Disposition'] = 'attachment; filename="output.docx"'
#
#         # Lưu tài liệu vào response
#         doc.save(response)
#         return response
#     else:
#         return HttpResponse("Method not allowed.", status=405)
#
#
#
# @csrf_exempt
# def convert_to_docx(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         content_html = data.get('content', '')
#
#         # Khởi tạo Document
#         doc = Document()
#
#         # Chia nhỏ nội dung thành từng đoạn (có thể tùy biến thêm)
#         for line in content_html.splitlines():
#             if line.strip():
#                 doc.add_paragraph(line)
#
#         # Tạo file tạm và gửi lại file .docx
#         response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#         response['Content-Disposition'] = 'attachment; filename="edited_ocr_result.docx"'
#         doc.save(response)
#         return response
#     return JsonResponse({"error": "Invalid request"}, status=400)


# def convert_images_view(request):
#     print("Received request to convert images")  # Để kiểm tra xem view có được gọi không
#     if request.method == 'POST':
#         uploaded_files = request.FILES.getlist('images[]')
#         print("Uploaded files:", uploaded_files)  # In ra các file đã upload
#
#         if not uploaded_files:
#             return redirect('ocr_picture')
#
#         # Chạy OCR
#         result_doc = process_uploaded_image(uploaded_files)
#         combined_text = "\n\n".join(result_doc)
#
#         return render(request, 'ocr_picture/result.html', {'text': combined_text})
#
#     return redirect('ocr_picture')


# def convert_images(request):
#     # Khởi tạo session để lưu trữ danh sách ảnh nếu chưa có
#     if 'uploaded_files' not in request.session:
#         request.session['uploaded_files'] = []
#
#     if request.method == 'POST' and request.FILES.getlist('images'):
#         images = request.FILES.getlist('images')  # Lấy danh sách file ảnh mới
#
#         # Thêm từng ảnh mới vào danh sách trong session
#         for image in images:
#             # Chỉ thêm ảnh nếu chưa có trong session
#             if image.name not in request.session['uploaded_files']:
#                 request.session['uploaded_files'].append(image.name)
#
#         # Cập nhật session để đảm bảo lưu lại danh sách ảnh
#         request.session.modified = True
#
#     # Tính số lượng file ảnh đã upload và lấy danh sách hiện tại
#     file_count = len(request.session['uploaded_files'])
#     uploaded_files = request.session['uploaded_files']
#
#     # Sau khi gửi kết quả, xóa session để tránh lưu lại cho lần upload sau
#     request.session.pop('uploaded_files', None)
#
#     # Trả về template với số lượng và danh sách tên file ảnh
#     return render(request, 'ocr_picture/result.html', {
#         'file_count': file_count,
#         'uploaded_files': uploaded_files
#     })
















