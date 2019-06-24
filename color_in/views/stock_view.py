from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from color_in.models import Stock


class StockObjectCreateView(CreateView):
    model = Stock
    fields = '__all__'


class StockObjectListView(ListView):
    model = Stock
    queryset = Stock.objects.filter(pk=1)


class StockObjectUpdateView(UpdateView):
    model = Stock
    queryset = Stock.objects.filter(pk=1)
    fields = '__all__'
    success_url = 'stock_status'

    def get_object(self):
        return get_object_or_404(Stock, pk=1)