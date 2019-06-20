from django.db import models


class AboutItem(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='about/')
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title


class Chef(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='chefs/', null=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    person_name = models.CharField(max_length=50, null=True, blank=True)
    person_title = models.CharField(max_length=50, null=True, blank=True)
    photo = models.ImageField(upload_to='testimonials/', null=True)
    content = models.TextField(null=True)

    def __str__(self):
        return self.person_name



