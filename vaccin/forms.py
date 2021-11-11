from django import forms
from .models import Vaccin


class VaccinForm(forms.ModelForm):
    class Meta:
        model = Vaccin
        fields = ['label', 'doses']

    def __init__(self, *args, **kwargs):
        super(VaccinForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'style': 'width: 50%'
            })
