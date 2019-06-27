from django.shortcuts import render
from .forms import ReservationForm
from django.shortcuts import HttpResponse
from .models import Reservation


def reserve_table(request):
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
    template = 'reservation/reservation_form.html'

    context = {
        'form': form
    }
    return render(request, template, context)
