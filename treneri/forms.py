from django import forms

from .models import Trener, UktsTrener


# class DateInput(forms.DateInput):
#     input_type = 'date'

class TreneriForm(forms.ModelForm):
    class Meta:
        model = UktsTrener
        fields = '__all__'
        labels = {
            'ime':'Ime',
        }
        # widgets = {
        #     'datum_rodjenja': DateInput(),
        # }

    def __init__(self, *args, **kwargs):
        super(TreneriForm,self).__init__(*args, **kwargs)
        # self.fields['klub'].empty_label = "Izaberi"
        # self.fields['klub'].required = False