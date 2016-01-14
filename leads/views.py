from django.views.generic import CreateView, UpdateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Lead
from .forms import LeadForm


class LeadsList(ListView):
    model = Lead
    template_name = 'leads/list.html'
    paginate_by = 5


class LeadAdd(CreateView):
    model = Lead
    form_class = LeadForm
    template_name = 'leads/create.html'
    success_url = '/'


class LeadDetail(DetailView):
    model = Lead
    template_name = 'leads/detail.html'


class LeadEdit(UpdateView):
    model = Lead
    template_name = 'leads/create.html'
    form_class = LeadForm
    success_url = '/'


class LeadDelete(DeleteView):
    model = Lead
    success_url = reverse_lazy('leads-list')
