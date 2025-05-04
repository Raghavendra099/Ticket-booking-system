from django.contrib import admin
from django.urls import path, include
from booking.views import home_view, UserLoginView  # import your custom login view
from django.contrib.auth.views import LogoutView  # ✅ Import Django's built-in logout view
from booking.views import home_view, UserLogoutView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name='home'),             # Routes to the booking app's home page
    path('booking/', include('booking.urls')),         # Includes all booking app routes
    path('login/', UserLoginView.as_view(), name='login'),  # Direct login URL

    # Auth URLs available directly
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='booking:login'), name='logout'),  
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
