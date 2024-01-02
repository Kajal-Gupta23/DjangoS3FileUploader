# myapp/admin.py

from django.contrib import admin
from .models import UploadedFile, FileUrl

@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'file')

@admin.register(FileUrl)
class FileUrlAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
