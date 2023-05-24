from django import forms
from .models import *

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('name', 'mobile_number', 'number_of_persons', 'date', 'time')




class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
