from django.views.generic.edit import FormView

from color_in.forms import ColorForm


class ColorView(FormView):
    template_name = 'color_in/color_form.html'
    form_class = ColorForm
    success_url = '/'

