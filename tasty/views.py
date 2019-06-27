from django.shortcuts import render
from about.models import AboutItem, Testimonial
from menu.models import Category, Dish
from blog.models import Article
from reservation.forms import ReservationForm
from reservation.models import Reservation
from django.shortcuts import HttpResponse


def home(request):
    about_item = AboutItem.objects.last()
    categories = Category.objects.all()
    dishes = Dish.objects.all()
    speciality_dishes = Dish.objects.filter(speciality=True)[:4]
    testimonials = Testimonial.objects.all()[:6]
    articles = Article.objects.all()

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            persons = form.cleaned_data['persons']
            try:
                Reservation.objects.create(name=name, phone=phone, email=email, date=date, time=time, persons=persons)
            except ValueError as e:
                return HttpResponse(e)
            # return redirect('contact:send_success')
    else:
        form = ReservationForm()

    template = 'home/index.html'
    context = {
        'about_item': about_item,
        'categories': categories,
        'dishes': dishes,
        'speciality_dishes': speciality_dishes,
        'testimonials': testimonials,
        'articles': articles,
        'form': form

    }
    return render(request, template, context)
