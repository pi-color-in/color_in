from django.db import models


class Stock(models.Model):
    stock_base = models.IntegerField()
    stock_black = models.IntegerField()
    stock_yellow = models.IntegerField()
    stock_magenta = models.IntegerField()
    stock_cyan = models.IntegerField()
    stock_status = models.BooleanField()
