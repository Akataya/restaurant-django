from django.shortcuts import render
from about.models import AboutItem, Testimonial
from menu.models import Category, Dish
from blog.models import Article


def home(request):
    about_item = AboutItem.objects.last()
    categories = Category.objects.all()
    dishes = Dish.objects.all()
    speciality_dishes = Dish.objects.filter(speciality=True)[:4]
    testimonials = Testimonial.objects.all()[:6]
    articles = Article.objects.all()
    template = 'home/index.html'
    context = {
        'about_item': about_item,
        'categories': categories,
        'dishes': dishes,
        'speciality_dishes': speciality_dishes,
        'testimonials': testimonials,
        'articles': articles
    }
    return render(request, template, context)
