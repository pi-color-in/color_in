from django.views.generic.edit import FormView
from color_in.forms import ColorForm


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
