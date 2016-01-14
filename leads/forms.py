from django.forms import ModelForm

from django.forms.widgets import TextInput, RadioSelect
from django.utils.safestring import mark_safe

from .models import Lead


class HorizRadioRenderer(RadioSelect.renderer):
    """ this overrides widget method to put radio buttons horizontally
        instead of vertically.
    """
    def render(self):
            """Outputs radios"""
            return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


class LeadForm(ModelForm):
    class Meta:
        model = Lead
        fields = ('__all__')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'card_number': TextInput(attrs={'class': 'form-control', 'placeholder': 'XXXXXXXXXXXXXXXX'}),
            'expiry_date': TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': RadioSelect(attrs={'class': 'radio-select'}, renderer=HorizRadioRenderer),
            'professional': RadioSelect(attrs={'class': 'radio-select'}, renderer=HorizRadioRenderer),
        }
