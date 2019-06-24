from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Stock(models.Model):
    stock_base = models.IntegerField(verbose_name='Base (Branco)', validators=[
                                     MinValueValidator(0), MaxValueValidator(100)])
    stock_black = models.IntegerField(verbose_name='Preto',
                                      validators=[MinValueValidator(0), MaxValueValidator(100)])
    stock_yellow = models.IntegerField(verbose_name='Amarelo',
                                       validators=[MinValueValidator(0), MaxValueValidator(100)])
    stock_magenta = models.IntegerField(verbose_name='Magentas',
                                        validators=[MinValueValidator(0), MaxValueValidator(100)])
    stock_cyan = models.IntegerField(verbose_name='Ciano',
                                     validators=[MinValueValidator(0), MaxValueValidator(100)])
    stock_status = models.BooleanField(verbose_name='Status')
