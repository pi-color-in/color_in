from django.views.generic.edit import CreateView
from django.views.generic import ListView

from color_in.models import Stock


class StockObjectCreateView(CreateView):
    model = Stock
    fields = '__all__'


class StockObjectListView(ListView):
    model = Stock
    queryset = Stock.objects.filter(pk=1)
