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



class PrijavaForm(forms.Form):
    ime = forms.CharField(required=True, label='First name*')
    prezime = forms.CharField(required=True, label='Last name*')
    telefon = PhoneNumberField(required=True, label='Your phone number*')
    email = forms.CharField(required=True, label='Your email*')
    drzava = CountryField(blank_label='(Choose your country)*').formfield()
    message = forms.CharField(widget = forms.Textarea, max_length = 2000, required=False, label='Do you have any additional questions? Ask us!')

    def __init__(self, *args, **kwargs):
        super(PrijavaForm, self).__init__(*args, **kwargs)

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
            Div('drzava', css_class="form-control bg-light"),
            Div('message', css_class="form-control bg-light"),
            )
        )
