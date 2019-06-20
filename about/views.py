from django.shortcuts import render
from .models import AboutItem, Chef


def about(request):
    about_item = AboutItem.objects.last()
    chefs = Chef.objects.all()
    template = 'about/about.html'
    context = {
        'about_item': about_item,
        'chefs': chefs
    }
    return render(request, template, context)
