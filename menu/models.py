from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=20)
    icon = models.CharField(max_length=20)
    css_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    category = models.ForeignKey(Category, models.SET_NULL, null=True)
    ingridients = models.CharField(max_length=100)
    description = models.TextField(max_length=100, null=True, blank=True)
    speciality = models.BooleanField(default=False)
    image = models.ImageField(upload_to="menu/", default="default_dish.png")
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Dish, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    # Add Flaticon credit:  <div>Icons made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">
    # Smashicons</a> from <a href="https://www.flaticon.com/"
    # title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/"
    # title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>
