from django import forms
from .models import Reservation
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit, Fieldset, ButtonHolder, Div
from django.utils.translation import ugettext_lazy as _
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput

#
# from functools import partial
# DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class ReservationForm(forms.ModelForm):
    name = forms.CharField(label=False, widget=forms.TextInput(
        attrs={'placeholder': _('Name'), 'class': 'form-control col-md-10'}))
    email = forms.EmailField(label=False, widget=forms.EmailInput(
        attrs={'placeholder': _('Email'), 'class': 'form-control col-md-10'}))
    phone = forms.CharField(label=False, widget=forms.TextInput(
        attrs={'placeholder': _('Phone'), 'class': 'form-control col-md-10'}))
    time = forms.TimeField(label=False,
                           input_formats=['%I:%M %p'],
                           widget=TimePickerInput(
                               format='%I:%M %p',
                               attrs={'placeholder': 'Time', 'class': 'form-control col-md-8'}))
    date = forms.DateField(label=False,
                           input_formats=['%m/%d/%Y'],
                           widget=DatePickerInput(
                               format='%m/%d/%Y',
                               attrs={'placeholder': 'Date', 'class': 'form-control col-md-8'}))
    persons = forms.IntegerField(label=False,
                                 widget=forms.TextInput(
                                     attrs={'placeholder': _('# Persons'), 'class': 'form-control col-md-10'}))

    class Meta:
        model = Reservation
        fields = '__all__'


    # Alternative to Bootstrap 4 form:
    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
    #     # 1. Settings for the reservation page:
    #     self.helper = FormHelper()
    #     self.helper.form_class = 'form-inline'
    #     self.helper.add_input(Submit('submit', 'Make a reservation', css_class='btn-lg'))
    #     # Use labels as placeholders
    #     layout = self.helper.layout = Layout()
    #     for field_name, field in self.fields.items():
    #         if field_name == 'name' or field_name == 'email' or field_name == 'phone':
    #             placeholder = 'Your {}'.format(field.label.title())
    #         elif field_name == 'persons':
    #             placeholder = 'Number of persons (1-100)'
    #         else:
    #             placeholder = field.label.title()
    #         layout.append(Div(Field(field_name, placeholder=placeholder, css_class='form-control'),
    #                           css_class='form-group col-md-6'))
    #     # 2. Settings for other pages + JavaScript:
    #     self.fields['name'] = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _('Name'), 'class': 'form-control col-md-10'}))
    #     self.fields['email'] = forms.EmailField(widget=forms.EmailInput(
    #         attrs={'placeholder': _('Email'), 'class': 'form-control col-md-10'}))
    #     self.fields['phone'] = forms.CharField(widget=forms.TextInput(
    # #         attrs={'placeholder': _('Phone'), 'class': 'form-control col-md-10'}))
    #     self.fields['date'] = forms.DateField(widget=forms.DateInput(
    #         attrs={'id': 'book_date', 'placeholder': _('Date'), 'class': 'form-control col-md-10'}))
    #     # self.fields['time'] = forms.TimeField(widget=forms.DateInput(
    #     #     attrs={'id': 'book_time', 'placeholder': _('Time'), 'class': 'form-control col-md-10 timepicker'}))
    #     self.fields['time'] = forms.TimeField(widget=TimePickerInput())
    #     self.fields['persons'] = forms.IntegerField(widget=forms.TextInput(
    #         attrs={'placeholder': _('# of Persons'), 'class': 'form-control col-md-12'}))
    #     for field_name, field in self.fields.items():
    #         field.label = False
