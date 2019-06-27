from django import forms
from django_comments_xtd.forms import XtdCommentForm
from django.utils.translation import ugettext_lazy as _
from django_comments_xtd.conf import settings

class CustomCommentForm(XtdCommentForm):
    def __init__(self, *args, **kwargs):
        comment = kwargs.pop("comment", None)
        if comment:
            initial = kwargs.pop("initial", {})
            initial.update({"reply_to": comment.pk})
            kwargs["initial"] = initial
            followup_suffix = ('_%d' % comment.pk)
        else:
            followup_suffix = ''
        super(CustomCommentForm, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(
            widget=forms.TextInput(attrs={'placeholder': _('Your name'),
                                          'class': 'form-control'}))
        self.fields['email'] = forms.EmailField(
            label=_("Mail"), help_text=_("Required for comment verification"),
            widget=forms.TextInput(attrs={'placeholder': _('Your email Address'),
                                          'class': 'form-control'}))
        self.fields['url'] = forms.URLField(
            label=_("Link"), required=False,
            widget=forms.TextInput(attrs={
                'placeholder': _('URL your name links to (optional)'),
                'class': 'form-control'}))
        self.fields['comment'] = forms.CharField(
            widget=forms.Textarea(attrs={'placeholder': _('Your comment'),
                                         'class': 'form-control'}),
            max_length=settings.COMMENT_MAX_LENGTH)
