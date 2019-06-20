from django.shortcuts import render
from .models import Category, Dish


def get_menu(request):
    categories = Category.objects.all()
    dishes = Dish.objects.all()
    template = 'menu/menu.html'
    context = {
        'categories': categories,
        'dishes': dishes
    }
    return render(request, template, context)


def specialities(request):
    speciality_dishes = Dish.objects.filter(speciality=True)
    template = 'menu/speciality_dishes.html'
    context = {
        'speciality_dishes': speciality_dishes
    }
    return render(request, template, context)

