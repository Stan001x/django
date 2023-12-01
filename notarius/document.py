from docx import Document
from django.db import models




def MakeReport():
    doc = models.FileField(null=True, upload_to='documents')
    document = Document('existing-document-file.docx')
    document.save('new-file-name.docx')
