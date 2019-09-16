from django import forms
from django.core import validators


def must_be_empty(value):
    if value:
        raise forms.ValidationError('is not empty, Bad bot!')


class SuggestionForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Please verify your email address")
    suggestion = forms.CharField(widget=forms.Textarea)
    honeypot = forms.CharField(label='Leave empty', widget=forms.HiddenInput, required=False, validators=[must_be_empty])

    def clean(self):
        cleaned_data = super(SuggestionForm, self).clean()
        email = cleaned_data['email']
        verify = cleaned_data.get('verify_email')

        if email != verify:
            raise forms.ValidationError('You need to enter the same email in both fields')



