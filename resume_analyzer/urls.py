from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('change-password/', views.change_password, name='change_password'),
    path('analyze/', views.analyze_ui, name='analyze_ui'),
    path('analyze/<int:id>', views.analyze_process_ui, name='analyze_process_ui'),
]
