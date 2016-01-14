from django.conf.urls import patterns, url

from .views import LeadsList, LeadAdd, LeadDetail, LeadEdit, LeadDelete, LeadsListDelete

urlpatterns = patterns(
    '',
    url(r'^add/$', LeadAdd.as_view(), name='lead-add'),
    url(r'^edit/(?P<pk>[0-9]+)/$', LeadEdit.as_view(), name='lead-edit'),
    url(r'^delete/(?P<pk>[0-9]+)/$', LeadDelete.as_view(), name='lead-delete'),
    url(r'^delete/$', LeadsListDelete.as_view(), name='leads-delete'),
    url(r'^(?P<pk>[0-9]+)/$', LeadDetail.as_view(), name='lead-detail'),
    url(r'^$', LeadsList.as_view(), name='leads-list'),
)
