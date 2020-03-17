from django import forms
from django.core.exceptions import ValidationError


class AuthorForm(forms.Form):
    name=forms.CharField(max_length=100)
    email=forms.EmailField()
    active=forms.BooleanField(required=False)
    created_on=forms.DateTimeField()
    last_logged_in=forms.DateTimeField()


    def clean_name(self):
        name = self.cleaned_data['name']
        lower_name = name.lower()
        if lower_name=='author' or lower_name=='admin':
            raise ValidationError('name cant be author or admin')
        return lower_name

    def clean_email(self):
        return self.cleaned_data['email'].lower()