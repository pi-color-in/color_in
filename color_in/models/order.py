from django.db import models
from .color import Color


class Order(models.Model):
    demanded_colors = models.ManyToManyField(Color)
