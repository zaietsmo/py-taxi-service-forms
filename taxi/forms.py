from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Car, Manufacturer

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['model', 'manufacturer', 'drivers']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))

class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['name', 'country']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))
