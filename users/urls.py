from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile_update/', views.profileUpdate, name='profile_update'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('change_password/', views.UserPasswordChangeView.as_view(
        template_name='users/password_change.html'), name='passwordChange'),
    
    
    path('password_reset/', auth_views.PasswordResetView.as_view(
        success_url = reverse_lazy('password_reset_done'),
        template_name='users/password_reset.html', ), name='password_reset'),
    
    
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'), name='password_reset_done'),
    
    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
         success_url = reverse_lazy('password_reset_complete'),
        template_name='users/password_reset_confirm.html', ), name='password_reset_confirm'),
    
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
       
        template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    
]
