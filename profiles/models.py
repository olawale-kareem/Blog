from django.db import models

class FileUploads(models.Model):
    # image = models.FileField(upload_to='uploads') # accepts all type of file
    image = models.ImageField(upload_to='uploads') # accepts only image file

    class Meta:
        verbose_name_plural = 'FileUploads'

 
    
  
