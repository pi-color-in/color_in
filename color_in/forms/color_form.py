from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from color_in.models import Color


class ColorForm(forms.ModelForm):

    qt_cyan = forms.IntegerField(label='Ciano',
                                 validators=[MinValueValidator(0), MaxValueValidator(100)])
    qt_magenta = forms.IntegerField(label='Magenta',
                                    validators=[MinValueValidator(0), MaxValueValidator(100)])
    qt_yellow = forms.IntegerField(label='Amarelo',
                                   validators=[MinValueValidator(0), MaxValueValidator(100)])
    qt_key = forms.IntegerField(label='Preto',
                                validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        model = Color
        fields = ['color_name']


    # def save(self, commit=True):
    #     print('DEBUG')
    #     cyan = self.cleaned_data['qt_cyan']
    #     magenta = self.cleaned_data['qt_magenta']
    #     yellow = self.cleaned_data['qt_yellow']
    #     key = self.cleaned_data['qt_key']
        
    #     color = super().save()
    #     return color
    #     color.cmyk = ','.join(map(str, [cyan, magenta, yellow, key]))
    #     color.save()
    #     return color
