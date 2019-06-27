from django import template
from ..models import SocialMediaLink, ContactDetails, ScheduleItem
from ..forms import SubscriberForm
from django.shortcuts import HttpResponseRedirect, reverse, redirect

register = template.Library()


@register.simple_tag
def get_social_media():
    social_media_links = SocialMediaLink.objects.all()
    return social_media_links


@register.simple_tag
def get_contact_details():
    contact_details = ContactDetails.objects.last()
    return contact_details


@register.simple_tag
def get_schedule():
    schedule_items = ScheduleItem.objects.all()
    return schedule_items


@register.simple_tag(takes_context=True)
def get_subscriber_form(context):
    request = context['request']
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            form = SubscriberForm()
    else:
        form = SubscriberForm()
    return form
