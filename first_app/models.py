from django.db import models

# Create your models here.

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    converted_file = models.FileField(blank=True, null=True, upload_to='converted/')
    created_at = models.DateTimeField(auto_now_add=True)
