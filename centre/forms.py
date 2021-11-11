from django import forms
from .models import Centre


class CentreForm(forms.ModelForm):
    class Meta:
        model = Centre
        fields = ['label', 'adresse']

    def __init__(self, *args, **kwargs):
        super(CentreForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'style': 'width: 50%'
            })
