from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse
from .models import Team

class CustomAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        # Check if a team exists where the leader's email is the user's email
        user_has_team = Team.objects.filter(lead_email=request.user.email).exists()

        if user_has_team:
            # User already has a team, send them to the homepage
            return '/'
        else:
            # User has no team, send them to the team creation form
            return reverse('core:register_team')