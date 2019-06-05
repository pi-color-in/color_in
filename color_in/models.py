from django.db import models


class Color(models.model):
    color_name = models.charField(max_length=100)
    qt_cyan = models.IntegerField()
    qt_magenta = models.IntegerField()
    qt_yellow = models.IntegerField()
    qt_black = models.IntegerField()


class Order(models.model):
    pass


class Stock(models.model):
    pass


class StockObserver(models.model):
    pass
