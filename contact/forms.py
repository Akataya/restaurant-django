from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit
from .models import Subscriber


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Your Name")
    email_address = forms.EmailField(required=True, label="Your email")
    subject = forms.CharField(required=True, label="Message subject")
    message = forms.CharField(widget=forms.Textarea, required=True, label="Your message", min_length=50)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # Remove labels
        self.helper.form_show_labels = False
        # Add the submit button
        self.helper.add_input(Submit('submit', 'Submit'))
        # Use labels as placeholders
        layout = self.helper.layout = Layout()
        for field_name, field in self.fields.items():
            layout.append(Field(field_name, placeholder=field.label.title()))


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']

    # Alternative to Bootstrap 4 form:
    def __init__(self, *args, **kwargs):
        super(SubscriberForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Subscribe'
        self.fields['email'].label = False
