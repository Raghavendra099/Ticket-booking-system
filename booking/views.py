from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Ticket, Flight, Train, Bus
from .forms import BookingForm
import stripe
from django.urls import reverse_lazy

# Stripe configuration
stripe.api_key = 'your_stripe_secret_key'  # Replace with your real secret key

# ---------------------- Static Pages ----------------------
def home_view(request):
    return render(request, 'booking/home.html')

def about(request):
    return render(request, 'booking/about.html')

# ---------------------- Tickets Views ----------------------
def flight_ticket_view(request):
    if not Flight.objects.exists():
        for i in range(1, 26):
            Flight.objects.create(
                airline_name=f"Airline {i}",
                source=f"City {i}",
                destination=f"City {i + 1}",
                departure_time=f"2025-05-0{i % 10} 10:00:00",
                arrival_time=f"2025-05-0{i % 10} 12:00:00",
                price=1000 + i * 50
            )
        print("Dummy flight data created!")

    flights = Flight.objects.all()
    return render(request, 'booking/flight_tickets.html', {'flights': flights})

def train_tickets(request):
    trains = Train.objects.all()
    return render(request, 'booking/train_tickets.html', {'trains': trains})

def bus_ticket_view(request):
    buses = Bus.objects.all()
    return render(request, 'booking/bus_tickets.html', {'buses': buses})

# ---------------------- Ticket Booking ----------------------
def book_ticket(request):
    if request.method == 'POST':
        passenger_name = request.POST.get('passenger_name')
        journey_date = request.POST.get('journey_date')
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        seat_number = request.POST.get('seat_number')
        price = request.POST.get('price')
        name = request.POST.get('name')
        travel_type = request.POST.get('travel_type')

        Ticket.objects.create(
            passenger_name=passenger_name,
            journey_date=journey_date,
            source=source,
            destination=destination,
            seat_number=seat_number,
            price=price,
            name=name,
            travel_type=travel_type
        )
        messages.success(request, "Ticket booked successfully!")
        return redirect('booking:book_ticket')

    return render(request, 'booking/book_ticket.html')

def book_ticket_selected(request, ticket_type, ticket_id):
    model_map = {
        'flight': Flight,
        'train': Train,
        'bus': Bus,
    }
    model = model_map.get(ticket_type)
    ticket = get_object_or_404(model, id=ticket_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            messages.success(request, f"{ticket_type.capitalize()} ticket booked successfully!")
            return redirect('booking:home')
    else:
        form = BookingForm()

    return render(request, 'booking/book_ticket.html', {
        'form': form,
        'ticket': ticket,
        'ticket_type': ticket_type
    })

def book_ticket_form(request):
    return render(request, 'booking/book_ticket_form.html', {
        'train_name': 'Shatabdi Express',
        'source': 'Gadag',
        'destination': 'Bangalore',
        'departure_time': '08:00 AM',
        'arrival_time': '02:00 PM',
        'price': 750,
        'STRIPE_PUBLISHABLE_KEY': 'your_test_publishable_key',
        'client_secret': 'your_stripe_client_secret',
    })

# ---------------------- Delete Ticket ----------------------
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('booking:home')
    return render(request, 'booking/delete.html', {'ticket': ticket})

# ---------------------- Chatbot ----------------------
def chatbot_response(request):
    if request.method == 'POST':
        prompt = request.POST.get("prompt")
        answer = get_ai_suggestion(prompt)  # Ensure get_ai_suggestion is defined/imported
        return JsonResponse({'response': answer})
    return render(request, "booking/chat.html")

# ---------------------- Stripe Payment ----------------------
@csrf_exempt
def create_checkout_session(request):
    if request.method == 'POST':
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': 'Ticket Booking'},
                    'unit_amount': 5000,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:8000/success/',
            cancel_url='http://localhost:8000/cancel/',
        )
        return JsonResponse({'id': session.id})

# ---------------------- Ticket List ----------------------
def flight_tickets(request):
    flights = Flight.objects.all()
    return render(request, 'booking/flight_tickets.html', {'flights': flights})

def train_tickets(request):
    trains = Train.objects.all()
    return render(request, 'booking/train_tickets.html', {'trains': trains})

def bus_tickets(request):
    buses = Bus.objects.all()
    return render(request, 'booking/bus_tickets.html', {'buses': buses})

# ---------------------- Authentication Views ----------------------
class UserLoginView(LoginView):
    template_name = 'booking/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('booking:home')

    def form_valid(self, form):
        messages.success(self.request, "Login successful!")
        return redirect('booking:home')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('booking:login')
