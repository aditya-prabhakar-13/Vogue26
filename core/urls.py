from django.urls import path
from . import views

# This is important for organization
app_name = 'core'

urlpatterns = [
    # This pattern will create the final URL: /core/register-team/
    path('register-team/', views.register_team, name='register_team'),
    path('register-for/<str:competition_name>/', views.register_for_competition_view, name='register_for_competition'),
    # This pattern will create the final URL: /core/success/
    path('success/', views.success_view, name='success'),
]
