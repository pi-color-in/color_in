from django.db import models


class Color(models.Model):
    color_name = models.CharField(max_length=100)
    cmyk = models.CharField(max_length=20) # it's gonna work as a comma-delimited list
