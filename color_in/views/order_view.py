from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView

from color_in.models import Order, Color
from color_in.views import arduino


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


def execute_order(request, *args, **kwargs):
    order_id = kwargs['pk']
    order_object = Order.objects.get(pk=order_id)
    color = Color.objects.get(pk=order_object.ordered_color_id)

    cmyk = color.cmyk
    c, m, y, k = map(int, cmyk.split(','))
    arduino.main(order_object.quantity, c, m , y, k)
