from django.shortcuts import render, redirect
from . models import *
from .forms import *

# Create your views here.
def index(request):
    popular_menu=PopularMenu.objects.all()
    context={
        'popular_menu':popular_menu
    }
    return render(request, 'index.html',context)



def book_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_table_success_page')  # Replace 'success_page' with the URL or name of the success page
    else:
        form = ReservationForm()
    
    return render(request, 'index.html', {'form': form})


def book_table_success_page(request):
    return render(request, 'book_table_success_page.html')


def about(request):
    return render(request, 'about.html')


def menu(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.select_related('category').all()
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'menu.html', context)



def gallery(request):
    return render(request, 'gallery.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})


def success(request):
    return render(request, 'success.html')