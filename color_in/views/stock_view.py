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


    def get_critical_colors(self):
        """
            Returns the colors whose quantity is critical (less or equal than 100ml)
        """
        critical_level = 100
        obj = Stock.objects.get(pk=1)

        all_levels = [(obj.stock_base, 'Branco'), (obj.stock_black, 'Preto'),
                      (obj.stock_yellow, 'Amarelo'), (obj.stock_magenta, 'Magenta'),
                      (obj.stock_cyan, 'Ciano')]

        # get all colors with critical level 
        critical_colors = filter(lambda tup: tup[0] <= critical_level, all_levels)

        # we're gonna just return their names so filter the level out
        critical_colors = list(map(lambda tup: tup[1], critical_colors))

        return critical_colors

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        critical_colors = self.get_critical_colors()
        data['critical_colors_list'] = critical_colors
        data['critical_colors'] = ", ".join(critical_colors)

        return data

class StockObjectUpdateView(UpdateView):
    model = Stock
    queryset = Stock.objects.filter(pk=1)
    fields = '__all__'
    success_url = 'stock_status'

    def get_object(self):
        return get_object_or_404(Stock, pk=1)
