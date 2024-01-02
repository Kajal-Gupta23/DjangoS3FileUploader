# myapp/models.py

from django.db import models

class FileUrl(models.Model):
    name = models.CharField(max_length=255, unique=True)
    url = models.URLField()

    def __str__(self):
        return self.name


class UploadedFile(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Create a FileUrl object with the name and URL
        file_url = FileUrl.objects.create(name=self.name, url=self.file.url)
        file_url.save()
