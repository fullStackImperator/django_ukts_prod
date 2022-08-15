# sendemail/forms.py
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from django_countries.fields import CountryField


from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap
from crispy_forms.bootstrap import InlineField, FormActions, StrictButton, Div
from crispy_forms.layout import Layout
from crispy_forms import bootstrap, layout

import datetime


class DateInput(forms.DateInput):
    input_type = 'date'

LICENCA_CHOICES =(
    ('', 'boja licence'),
    ("plava", "plava"),
    ("crvena", "crvena"),
)


class AplikacijaForm(forms.Form):
    ime = forms.CharField(required=True)
    prezime = forms.CharField(required=True)
    telefon = PhoneNumberField(required=True)
    email = forms.EmailField(required=True)
    adresa = forms.CharField(required=True)
    grad = forms.CharField(required=True)
    opstina = forms.CharField(required=True)
    broj_opstine = forms.CharField(required=True)
    drzava = CountryField(blank_label='(Izaberite drzavu)').formfield()
    slika = forms.FileField(required=False)

    broj_licence = forms.CharField(required=True)
    boja_licence = forms.ChoiceField(choices = LICENCA_CHOICES) # choice field

    zvanje_licenca = forms.CharField(widget=forms.TextInput, label='Zvanje koje piše na licenci', required=True)

    clan_od = forms.DateField(widget=DateInput, label='Član od') # DateField

    diploma = forms.FileField(required=False)

    diploma_broj = forms.CharField(widget=forms.Textarea, label='Diploma datum  i mesto izdavanja i broj diplome, akademsko zvanje (piše na diploma)', required=True)

    fakultet = forms.CharField(required=True, label='Fakultet koji je izdao')


    def __init__(self, *args, **kwargs):
        super(AplikacijaForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.use_custom_control = True
        # self.helper.form_tag = False
        # self.helper.method = "POST"
        # self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap4/layout/inline_field.html'
        # self.helper.form_action = "company:create-employee"

        self.helper.layout = Layout(
        Div(

            Div('ime', css_class="form-control bg-light"),
            Div('prezime', css_class="form-control bg-light"),
            Div('telefon', css_class="form-control bg-light"),
            Div('email', css_class="form-control bg-light"),
            Div('adresa', css_class="form-control bg-light"),
            Div('grad', css_class="form-control bg-light"),
            Div('opstina', css_class="form-control bg-light"),
            Div('broj_opstine', css_class="form-control bg-light"),
            Div('drzava', css_class="form-control bg-light"),
            Div('slika', css_class="form-control bg-light", title="Explication title"),
            Div('broj_licence', css_class="form-control bg-light"),
            Div('boja_licence', css_class="form-control bg-light"),
            Div('zvanje_licenca', css_class="form-control bg-light"),
            Div('clan_od', css_class="form-control bg-light"),
            Div('diploma', css_class="form-control bg-light"),
            Div('diploma_broj', css_class="form-control bg-light"),
            Div('fakultet', css_class="form-control bg-light"),
            # Div('middle_initial', css_class="col-sm-2"),
            # Div('social_security_number', css_class="col-sm-2"),
            # bootstrap.FormActions(
            #     layout.Submit('submit', 'Add', css_class='btn btn-primary')),
            # css_class='col-6',
            )
        )

    class Meta:
        labels = {
            'ime':'Ime',
        }
        widgets = {
            'clan_od': DateInput(),
        }