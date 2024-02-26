from django.shortcuts import render



#create your views here

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

def reservation(request):
    return render(request, 'reservation.html')

def gallery(request):
    return render(request, 'gallery.html')

def reviews(request):
    return render(request, 'reviews.html')

def contact(request):
    return render(request, 'contact.html')
