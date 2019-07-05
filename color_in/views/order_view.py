from django.views.generic.edit import CreateView
from django.views.generic import ListView

from color_in.models import Order


class OrderCreateView(CreateView):
    model = Order
    fields = '__all__'
    success_url = 'list_orders'

class OrderListView(ListView):
    model = Order
