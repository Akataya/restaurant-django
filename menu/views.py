from django.shortcuts import render, HttpResponse
from .models import Category, Dish
from reservation.forms import ReservationForm
from reservation.models import Reservation

def get_menu(request):
    categories = Category.objects.all()
    dishes = Dish.objects.all()
    form = ReservationForm()

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

    template = 'menu/menu.html'
    context = {
        'categories': categories,
        'dishes': dishes,
        'form': form
    }
    return render(request, template, context)


def specialities(request):
    speciality_dishes = Dish.objects.filter(speciality=True)
    template = 'menu/speciality_dishes.html'
    context = {
        'speciality_dishes': speciality_dishes
    }
    return render(request, template, context)

