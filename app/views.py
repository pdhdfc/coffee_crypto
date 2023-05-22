from django.shortcuts import render, redirect
from . models import *
# Create your views here.
def index(request):
    popular_menu=PopularMenu.objects.all()
    context={
        'popular_menu':popular_menu
    }
    return render(request, 'index.html',context)

from .forms import ReservationForm

from django.shortcuts import render, redirect
from .forms import ReservationForm

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