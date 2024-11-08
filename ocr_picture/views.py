import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from underthesea import word_tokenize
from django.conf import settings
from .ocr import process_uploaded_image
import os
from fuzzywuzzy import fuzz, process



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




# DICTIONARY_PATH = os.path.join(settings.BASE_DIR, 'ocr_picture', 'data', 'Viet74K.txt')
# # Load từ điển
# with open(DICTIONARY_PATH, "r", encoding="utf-8") as f:
#     VIETNAMESE_WORDS = set(word.strip().lower() for word in f.readlines())
#
# def find_closest_word(word, vocabulary, threshold=80):
#     """
#     Tìm từ gần nhất với `word` trong `vocabulary` với độ tương đồng >= threshold.
#     """
#     match, score = process.extractOne(word, vocabulary, scorer=fuzz.ratio)
#     if score >= threshold:
#         return match
#     return None

# @csrf_exempt
# def check_spell_view(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         content = data.get("content", "")
#
#         # Tách từ tiếng Việt
#         words = word_tokenize(content, format="text").split()
#
#         corrected_words = []
#         for word in words:
#             word_lower = word.lower()
#             if word_lower in VIETNAMESE_WORDS:
#                 # Nếu từ có trong từ điển, giữ nguyên
#                 corrected_words.append(word)
#             else:
#                 # Nếu từ không có trong từ điển, tìm từ gần nhất
#                 suggestion = find_closest_word(word_lower, VIETNAMESE_WORDS)
#                 corrected_words.append(suggestion if suggestion else word)
#
#         corrected_content = " ".join(corrected_words)
#
#         return JsonResponse({"corrected_content": corrected_content})
#
#     return JsonResponse({"error": "Invalid request"}, status=400)




















