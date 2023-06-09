from django.forms import ModelForm
from django import forms
from datetime import datetime

from monitoreo.models import Switch


class Switchform(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Switch
        fields = '__all__'
        widgets = {
            'ip': forms.TextInput(attrs={'class': 'form-control'}),
        }