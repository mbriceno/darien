from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['full_name', 'birthdate', 'years_old', 'nationality', 'address', 'email', 'phone', 'ptype', 'bank']

    def clean_birthdate(self):
        birthdate = self.cleaned_data['birthdate']
        if birthdate.year < 1900:
            raise ValidationError(_('Invalid birthdate'))
        return birthdate

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(phone) < 10:
            raise ValidationError(_('Invalid phone number'))
        return phone

