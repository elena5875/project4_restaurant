#views.py

from django.shortcuts import render, redirect
from .forms import ReservationForm

def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., save to database)
            # Redirect to confirmation page
            return redirect('confirmation_page')
    else:
        form = ReservationForm()
    return render(request, 'reservation.html', {'form': form})


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

def gallery(request):
    return render(request, 'gallery.html')

def reviews(request):
    return render(request, 'reviews.html')

def contact(request):
    return render(request, 'contact.html')

