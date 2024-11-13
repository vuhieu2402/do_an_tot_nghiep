from django import forms


LANGUAGE_CHOICES = [
    ('en', 'English'),
    ('vi', 'Vietnamese'),
    ('fr', 'Français'),
    ('es', 'Español'),
    ('ru', 'Русский'),
    ('ar', 'العربية'),
    ('zh', '中文'),
    ('ja', '日本語'),
    ('ko', '한국어'),
    ('pt', 'Português'),
    ('de', 'Deutsch'),
    ('it', 'Italiano'),
    ('nl', 'Nederlands'),
    ('pl', 'Polski'),
    ('sv', 'Svenska'),
    ('tr', 'Türkçe'),
    ('id', 'Bahasa Indonesia'),
    ('th', '��า��าไทย'),
    ('hu', 'Magyar'),
    ('cs', '��eština'),
]

class PDFUploadForm(forms.Form):
    pdf_file = forms.FileField(label="Chọn file PDF")
    source_language = forms.ChoiceField(choices=LANGUAGE_CHOICES, label="Ngôn ngữ gốc")
    target_language = forms.ChoiceField(choices=LANGUAGE_CHOICES, label="Ngôn ngữ muốn chuyển đổi")


class DOCXUploadForm(forms.Form):
    docx_file = forms.FileField(label="Chọn file DOCX")
    source_language = forms.ChoiceField(choices=LANGUAGE_CHOICES, label="Ngôn ngữ gốc")
    target_language = forms.ChoiceField(choices=LANGUAGE_CHOICES, label="Ngôn ngữ muốn chuyển đổi")
