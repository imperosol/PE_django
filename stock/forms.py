from django import forms
from .models import Stock


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['centre_id', 'vaccin_id', 'doses']

    def __init__(self, *args, **kwargs):
        super(StockForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'style': 'width: 50%'
            })
