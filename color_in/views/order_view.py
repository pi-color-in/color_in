from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView

from color_in.models import Order


class OrderCreateView(CreateView):
    model = Order
    fields = '__all__'
    success_url = 'list_orders'


class OrderListView(ListView):
    model = Order


class OrderDeleteView(DeleteView):
    model = Order
    success_url = '/list_orders'

    def get(self, request, *args, **kwargs):
        # ignore object confirmation template page
        return self.post(request, *args, **kwargs)
