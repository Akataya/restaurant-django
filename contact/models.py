from django.db import models


class ContactDetails(models.Model):
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Contact Details"
        verbose_name_plural = "Contact Details"

    def __str__(self):
        return str(self.id)


class SocialMediaLink(models.Model):
    name = models.CharField(max_length=25)
    link = models.URLField()

    def __str__(self):
        return self.name


WEEKDAY_CHOICES = (
    ("Monday", 'Mon'),
    ("Tuesday", 'Tue'),
    ("Wednesday", "Wed"),
    ("Thursday", "Thu"),
    ("Friday", "Fri"),
    ("Saturday", "Sat"),
    ("Sunday", "Sun"),
)


class ScheduleItem(models.Model):
    day = models.CharField(max_length=50, choices=WEEKDAY_CHOICES, unique=True)
    open_time = models.TimeField(null=True, blank=True)
    close_time = models.TimeField(null=True, blank=True)
    closed = models.BooleanField(default=False)

    def __str__(self):
        return self.day


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email
