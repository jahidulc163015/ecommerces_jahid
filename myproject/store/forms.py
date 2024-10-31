from django import forms
from.models import *

class  ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields={"name","email","message"}

class  BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields={"firstname","lastname","company","address","town","country","postcode","mobile","email"}
