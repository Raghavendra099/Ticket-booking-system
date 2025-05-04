from django.urls import path, include
from . import views
from .views import UserLoginView, UserLogoutView  # Import the views here
from django.contrib import admin
from django.contrib.auth import views as auth_views
app_name = 'booking'

urlpatterns = [
    # 🌐 Basic Pages
    path('', views.home_view, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page

    # Ticket Views # home.html
    path('flights/', views.flight_tickets, name='flight_tickets'),  # flight_tickets.html
    path('trains/', views.train_tickets, name='train_tickets'),  # train_tickets.html
    path('buses/', views.bus_tickets, name='bus_tickets'),  # bus_tickets.html
    path('book_ticket/<int:train_id>/<str:train_name>/<str:source>/<str:destination>/<str:departure_time>/<str:arrival_time>/<int:price>/', 
         views.book_ticket_form, name='book_ticket_form'),  # Booking detail

    path('bus-tickets/', views.bus_tickets, name='bus_tickets'),
    path('book-ticket/<int:ticket_id>/', views.book_ticket_form, name='book_ticket_form'),
    path('book_ticket_form/', views.book_ticket_form, name='book_ticket_form'),

    # Booking-related
    path('book_ticket/', views.book_ticket, name='book_ticket'),
 # Handle ticket booking
    path('book_ticket_selected/<ticket_type>/<int:ticket_id>/', views.book_ticket_selected, name='book_ticket_selected'),
    path('book_ticket/<int:train_id>/<str:train_name>/<str:source>/<str:destination>/<str:departure_time>/<str:arrival_time>/<int:price>/', views.book_ticket_form, name='book_ticket_form'),
    # booking/urls.py
    path('book_ticket/<ticket_type>/<int:ticket_id>/', views.book_ticket_form, name='book_ticket_form'),
    # ❌ Delete Ticket
    path('delete_ticket/<int:ticket_id>/', views.delete_ticket, name='delete_ticket'),

    # Chatbot
    path('chat/', views.chatbot_response, name='chat'),

    # Stripe Payment
    path('create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),

    # (Optional) Auth views can also be added here
    path('login/', UserLoginView.as_view(), name='login'),  # Login view
    path('logout/', UserLogoutView.as_view(), name='logout'),  # Logout view

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
