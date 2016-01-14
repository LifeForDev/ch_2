from django.forms import ModelForm, inlineformset_factory

from django.forms.widgets import TextInput, RadioSelect, HiddenInput
from django.forms.models import BaseInlineFormSet
from django.utils.safestring import mark_safe

from django.utils.encoding import force_text
from django.forms.utils import flatatt
from django.utils.html import format_html
from django.forms.formsets import DELETION_FIELD_NAME

from .models import Lead, Language


class HorizRadioRenderer(RadioSelect.renderer):
    """ this overrides widget method to put radio buttons horizontally
        instead of vertically.
    """
    def render(self):
            """Outputs radios"""
            return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


class AddableTextInput(TextInput):
    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        if value != '':
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_text(self._format_value(value))

        btn = '<span class="input-group-btn"><button class="btn add-form"><i class="fa fa-plus fa-fw"></i>Add</button></span>'
        input_group = '<div class="input-group"><input{} />{}</div>'.format('{}', btn)
        return format_html(input_group, flatatt(final_attrs))


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


class LanguageForm(ModelForm):
    class Meta:
        model = Language
        fields = ('name',)
        widgets = {
            'name': AddableTextInput(attrs={'class': 'form-control', 'placeholder': 'English'}),
        }
        labels = {
            'name': '',
        }


class RequiredFormSet(BaseInlineFormSet):
    """
    Makes first form in formset required
    """

    def __init__(self, *args, **kwargs):
        super(RequiredFormSet, self).__init__(*args, **kwargs)
        self.forms[0].empty_permitted = False

    def add_fields(self, form, index):
        # Hide delete checkbox from formset
        super(RequiredFormSet, self).add_fields(form, index)
        form.fields[DELETION_FIELD_NAME].widget = HiddenInput()


LanguageFormSet = inlineformset_factory(Lead, Language,
                                        form=LanguageForm, formset=RequiredFormSet, extra=1, can_delete=True)
