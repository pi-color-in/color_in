from django.views.generic.edit import FormView, DeleteView
from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponseRedirect

from color_in.forms import ColorForm, ColorEditForm
from color_in.models import Color

# TODO: remove duplicated code

def home_page(request):
    return HttpResponseRedirect("/list_colors")

class ColorView(FormView):
    template_name = 'color_in/color_form.html'
    form_class = ColorForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user

        # getting the colors in the form so we can insert comma-delimited
        cyan = form.cleaned_data['qt_cyan']
        magenta = form.cleaned_data['qt_magenta']
        yellow = form.cleaned_data['qt_yellow']
        key = form.cleaned_data['qt_key']

        color = form.save(commit=False) # don't commit yet, we need to change the cmyk column
        color.cmyk = ','.join(map(str, [cyan, magenta, yellow, key]))
        color.save()

        return super().form_valid(form)


class ColorEditView(FormView):
    template_name = 'color_in/color_form.html'
    form_class = ColorEditForm
    success_url = '/'

    def get_initial(self):
        """
            Returns the initial data to be used in the form
        """
        initial = super().get_initial()

        color_id = self.kwargs['pk']
        color_obj = Color.objects.get(id=color_id)
        cyan, magenta, yellow, key = color_obj.cmyk.split(',')

        initial['color_name'] = color_obj.color_name
        initial['qt_cyan'] = cyan
        initial['qt_magenta'] = magenta
        initial['qt_yellow'] = yellow
        initial['qt_key'] = key

        return initial

    def form_valid(self, form):
        color_id = self.kwargs['pk']

        color_obj = Color.objects.get(id=color_id)
        color_obj.color_name = form.cleaned_data['color_name']

        # getting the colors in the form so we can insert comma-delimited
        cyan = form.cleaned_data['qt_cyan']
        magenta = form.cleaned_data['qt_magenta']
        yellow = form.cleaned_data['qt_yellow']
        key = form.cleaned_data['qt_key']

        color_obj.cmyk = ','.join(map(str, [cyan, magenta, yellow, key]))
        color_obj.save()

        return super().form_valid(form)


class ColorListView(ListView):
    model = Color


class ColorDeleteView(DeleteView):
    model = Color
    success_url = '/list_colors'

    def get(self, request, *args, **kwargs):
        # ignore object confirmation template page
        return self.post(request, *args, **kwargs)