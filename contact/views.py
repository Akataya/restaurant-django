from django.shortcuts import render, redirect, HttpResponse
from .models import ContactDetails
from .forms import ContactForm, SubscriberForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.views.generic import CreateView


def contact(request):
    contact_details = ContactDetails.objects.last()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email_address']
            message = form.cleaned_data['message']
            try:
                send_mail(name, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            # return redirect('contact:send_success')
    else:
        form = ContactForm()
    template = 'contact/contact.html'
    context = {
        'contact_details': contact_details,
        'form': form
    }
    return render(request, template, context)


def send_success(request):
    return HttpResponse('Thank you for your email!')