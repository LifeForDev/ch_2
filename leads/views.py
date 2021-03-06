from django.views.generic import CreateView, UpdateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from .models import Lead
from .forms import LeadForm, LanguageFormSet


class LeadsList(ListView):
    model = Lead
    template_name = 'leads/list.html'
    paginate_by = 5


class LeadAdd(CreateView):
    model = Lead
    form_class = LeadForm
    template_name = 'leads/create.html'

    def get_context_data(self, **kwargs):
        context = super(LeadAdd, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = LanguageFormSet(self.request.POST)
        else:
            context['formset'] = LanguageFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(reverse('leads-list'))
        else:
            return self.render_to_response(self.get_context_data(form=form))


class LeadDetail(DetailView):
    model = Lead
    template_name = 'leads/detail.html'


class LeadEdit(UpdateView):
    model = Lead
    template_name = 'leads/create.html'
    form_class = LeadForm

    def get_context_data(self, **kwargs):
            context = super(LeadEdit, self).get_context_data(**kwargs)
            if self.request.POST:
                context['formset'] = LanguageFormSet(self.request.POST, instance=self.object)
            else:
                context['formset'] = LanguageFormSet(instance=self.object)
            return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            print formset.save()
            return redirect(reverse('leads-list'))
        else:
            return self.render_to_response(self.get_context_data(form=form))


class LeadDelete(DeleteView):
    model = Lead
    template_name = 'leads/confirm_delete_leads.html'
    success_url = reverse_lazy('leads-list')


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
        if not self.leads_to_delete:
            return HttpResponseRedirect(self.success_url)
        if self.request.POST.get("confirm_delete"):
            queryset = self.get_queryset()
            queryset.delete()
            return HttpResponseRedirect(self.success_url)
        elif self.request.POST.get("cancel"):
            return HttpResponseRedirect(self.success_url)
        else:
            return self.get(self, *args, **kwargs)
