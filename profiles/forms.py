from django import forms
from django.db.models import fields
from .models import FileUploads 

# manual form
# class FileForm(forms.Form):
#     image = forms.FileField()

# modal form
class FileForm(forms.ModelForm):
    class Meta:
        model = FileUploads
        fields = '__all__'