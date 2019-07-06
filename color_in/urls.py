"""color_in URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from color_in.views import (
    ColorView,
    ColorEditView,
    ColorListView,
    StockObjectCreateView,
    StockObjectListView,
    StockObjectUpdateView,
    OrderCreateView,
    OrderListView,
    OrderDeleteView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_color/', ColorView.as_view(), name='color-add'),
    path('edit_color/<int:pk>', ColorEditView.as_view(), name='color-edit'),
    path('list_colors/', ColorListView.as_view(), name='color-list'),
    path('stock_create', StockObjectCreateView.as_view(), name='stock-create'),
    path('stock_status', StockObjectListView.as_view(), name='stock-status'),
    path('change_stock', StockObjectUpdateView.as_view(), name='stock-change'),
    path('create_order', OrderCreateView.as_view(), name='create-order'),
    path('list_orders', OrderListView.as_view(), name='list-orders'),
    path('delete_order/<int:pk>', OrderDeleteView.as_view(), name='delete-order')
]
