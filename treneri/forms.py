from django import forms

from .models import Trener


class TreneriForm(forms.ModelForm):
    class Meta:
        model = Trener
        fields = '__all__'
        labels = {
            'ime':'Ime',
        }

    def __init__(self, *args, **kwargs):
        super(TreneriForm,self).__init__(*args, **kwargs)
        self.fields['klub'].empty_label = "Izaberi"
        self.fields['klub'].required = False