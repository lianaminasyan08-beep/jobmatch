from django import forms

class UploadResumeForm(forms.Form):
    file = forms.FileField()