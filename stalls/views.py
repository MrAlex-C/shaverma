from stalls.models import Stall
from stalls.forms import StallListForm
from django.views import generic


class StallsList(generic.ListView):

    template_name = 'stalls/stall_list.html'
    model = Stall

    def dispatch(self, request, *args, **kwargs):
        self.form = StallListForm(request.GET)
        self.form.is_valid()
        return super(StallsList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Stall.objects.all()
        if self.form.cleaned_data.get('search'):
            queryset = queryset.filter(name__icontains=self.form.cleaned_data['search'])
        if self.form.cleaned_data.get('sort_field'):
            queryset = queryset.order_by(self.form.cleaned_data['sort_field'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super(StallsList, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context