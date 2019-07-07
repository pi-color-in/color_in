from django.db import models
from .color import Color


class Order(models.Model):
    """
        Represents an order in the application
    """
    ordered_color = models.ForeignKey(
        Color, on_delete=models.DO_NOTHING, verbose_name="Cor desejada", blank=False, default=None)
    quantity = models.IntegerField(verbose_name="Quantidade", blank=False)
