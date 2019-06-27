from django.contrib import admin
from .models import ContactDetails, SocialMediaLink, ScheduleItem, Subscriber


admin.site.register(ContactDetails)
admin.site.register(SocialMediaLink)
admin.site.register(ScheduleItem)
admin.site.register(Subscriber)