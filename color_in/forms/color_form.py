from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from color_in.models import Color


class ColorForm(forms.ModelForm):

    class Meta:
        model = Color
        fields = ['color_name']

    qt_cyan = forms.IntegerField(label='Ciano',
                                 validators=[MinValueValidator(0), MaxValueValidator(100)])
    qt_magenta = forms.IntegerField(label='Magenta',
                                    validators=[MinValueValidator(0), MaxValueValidator(100)])
    qt_yellow = forms.IntegerField(label='Amarelo',
                                   validators=[MinValueValidator(0), MaxValueValidator(100)])
    qt_key = forms.IntegerField(label='Preto',
                                validators=[MinValueValidator(0), MaxValueValidator(100)])

    
