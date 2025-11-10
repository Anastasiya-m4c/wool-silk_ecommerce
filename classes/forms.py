from django import forms
from .models import Class


class ClassForm(forms.ModelForm):

    class Meta:
        model = Class
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
