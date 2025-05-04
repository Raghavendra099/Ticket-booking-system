from django import forms
from .models import Ticket
from django.contrib.auth.forms import AuthenticationForm

# Update BookingForm to use the correct field names
class BookingForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['passenger_name', 'journey_date', 'source', 'destination', 'seat_number', 'price']

# Custom login form (you can keep this as it is)
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w-full p-2 border rounded'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'w-full p-2 border rounded'})
    )

# Remove the second BookingForm (the one with full_name, email, and phone) unless it is required for something else.
# If you want this form to be separate, you can rename it or remove it if it's unnecessary.
