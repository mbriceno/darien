from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Credit, Bank


class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ['name', 'btype', 'address']

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 5:
            raise forms.ValidationError(_('Name must be at least 5 characters long.'))
        return name


class CreditForm(forms.ModelForm):
    class Meta:
        model = Credit
        fields = ['client', 'bank', 'description', 'credit_amount', 'min_payment', 'max_payment', 'credit_term', 'ctype']

    def clean(self):
        cleaned_data = super().clean()
        min_payment = cleaned_data.get('min_payment')
        max_payment = cleaned_data.get('max_payment')
        if min_payment > max_payment:
            raise ValidationError(_('Minimum payment cannot be greater than maximum payment'))
        return cleaned_data
