__author__ = 'sbodduluri2'
#forms.py
from django import forms
#
class UploadFileForm(forms.Form):
    file  = forms.FileField(required='True')