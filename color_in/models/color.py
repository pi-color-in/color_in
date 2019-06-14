from django.db import models
from django.core.validators import validate_comma_separated_integer_list


class Color(models.Model):
    """
        Represents a Color object

        Fields: color_name, cmyk (comma-delimited list)
    """
    color_name = models.CharField(max_length=100)
    cmyk = models.CharField(max_length=20,
                            validators=[validate_comma_separated_integer_list])
