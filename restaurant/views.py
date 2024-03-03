#views.py

from django.shortcuts import render, redirect
from .forms import ReservationForm

def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., save to database)
            # For now, let's assume we don't save the form data, just render a confirmation message
            return render(request, 'reservation_confirmation.html')  # Render the confirmation template
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

