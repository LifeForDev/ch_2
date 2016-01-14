from django.views.generic import CreateView, UpdateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

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
    # template_name = 'leads/confirm_delete_leads.html'
    success_url = reverse_lazy('leads-list')
    # leads_to_delete = []


class LeadsListDelete(DeleteView):
    model = Lead
    template_name = 'leads/confirm_delete_leads.html'
    success_url = reverse_lazy('leads-list')
    leads_to_delete = []

    def get_queryset(self):
        queryset = super(LeadsListDelete, self).get_queryset()
        self.queryset = queryset.filter(id__in=self.leads_to_delete)
        return self.queryset

    def get_object(self, queryset=None):
        return self.get_queryset()

    def post(self, request, *args, **kwargs):
        self.leads_to_delete = self.request.POST.getlist('leadsToDelete')
        print '-----------------+++++++++++'
        print self.leads_to_delete
        if self.request.POST.get("confirm_delete"):
            queryset = self.get_queryset()
            queryset.delete()
            return HttpResponseRedirect(self.success_url)
        elif self.request.POST.get("cancel"):
            return HttpResponseRedirect(self.success_url)
        else:
            return self.get(self, *args, **kwargs)

# class SomeItemConfirmDeleteView(DeleteView):
#     template_name = 'confirm_delete_someitems.html'
#     model = SomeItem
#     success_url = reverse_lazy('list_someitems_url')
#     items_to_delete = []

#     def get_queryset(self):
#         queryset = super(ChargeParkConfirmDeleteView, self).get_queryset()
#         self.queryset = queryset.filter(id__in=self.items_to_delete)
#         return self.queryset

#     def get_object(self, queryset=None):
#         return self.get_queryset()

#     def post(self, request, *args, **kwargs):
#         self.items_to_delete = self.request.POST.getlist('itemsToDelete')
#         if self.request.POST.get("confirm_delete"):
#             # when confirmation page has been displayed and confirm button pressed
#             queryset = self.get_queryset()
#             queryset.delete() # deleting on the queryset is more efficient than on the model object
#             return HttpResponseRedirect(self.success_url)
#         elif self.request.POST.get("cancel"):
#             # when confirmation page has been displayed and cancel button pressed
#             return HttpResponseRedirect(self.success_url)
#         else:
#             # when data is coming from the form which lists all items
#             return self.get(self, *args, **kwargs)
