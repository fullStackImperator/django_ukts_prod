from django import forms

from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

    # helper = FormHelper()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

    # overriding default form setting and adding bootstrap class
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'placeholder': 'Vaše ime','class':'form-control'}
        self.fields['email'].widget.attrs = {'placeholder': 'Vaš email', 'class':'form-control'}
        self.fields['body'].widget.attrs = {'placeholder': 'Unesi komentar ovde...', 'class':'form-control', 'rows':'5'}
        self.fields['name'].label = "Ime"
        self.fields['body'].label = "Komentar"

class SearchForm(forms.Form): 
    query = forms.CharField()