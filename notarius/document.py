from docx import Document
from django.db import models
from django import forms




def MakeReport():
    doc = models.FileField(null=True, upload_to='documents')
    document = Document('existing-document-file.docx')
    document.save('new-file-name.docx')
