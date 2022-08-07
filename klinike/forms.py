from django import forms
from django.forms import ModelForm

from .models import Photo, Klinike

class UploadForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['slike'] = forms.FileField(widget=forms.ClearableFileInput(attrs={"multiple": True}))


    class Meta:
        model = Photo
        fields = '__all__'
        exclude = ['naslov', 'tip', 'slika']
        # fields = ['godina', 'slike']
