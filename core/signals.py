# core/signals.py

from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from .models import UserProfile

@receiver(user_signed_up)
def user_signed_up_receiver(request, user, **kwargs):
    """
    When a user signs up via a social account, create a UserProfile,
    populate it, and save the email to the session for the redirect.
    """
    try:
        sociallogin = kwargs.get('sociallogin')
        if sociallogin:
            # Get the profile picture URL
            picture_url = sociallogin.account.extra_data.get('picture')
            UserProfile.objects.create(user=user, profile_pic_url=picture_url)
            
            # --- ADD THESE TWO LINES ---
            # Get the email from the reliable sociallogin object
            email = sociallogin.account.extra_data.get('email', '')
            # Store it in the session to use on the next page
            request.session['social_login_email'] = email
            # --------------------------

    except Exception as e:
        print(f"Error in user_signed_up_receiver: {e}")
        # Still try to create a profile even if there's an error
        if not hasattr(user, 'userprofile'):
            UserProfile.objects.create(user=user)