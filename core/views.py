from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TeamForm, MemberFormSet
from .models import Competition, Team
from django.core.mail import send_mail


def landing_page(request):

    if request.user.is_authenticated:
        # --- NEW LOGIC ---
        # Check if the user has already registered a team
        # try:
        #     user_has_team = Team.objects.filter(lead_email=request.user.email).exists()
        # except Exception:
        #     # Handle potential errors if user has no email (shouldn't happen with our setup)
        #     user_has_team = False

        # if user_has_team:
        #     # If they have a team, just show the landing page (as a "homepage")
        #     return render(request, 'core/landing.html')
        # else:
        #     # If they are logged in and have NO team, redirect to the registration form
        #     return redirect('core:register_team')
        # --- END NEW LOGIC ---
        return redirect('core:register_team')
    
    # If the user is not logged in, show the landing page (with register buttons)
    return render(request, 'core/landing.html')



@login_required
def register_team(request):
    """
    Handles the registration of a new team and its members.
    Pre-fills the competition based on the session and sends a confirmation email.
    """
    # Get the user's email from the session (most reliable) or the user object
    user_email = request.session.get('social_login_email', request.user.email)

    if request.method == 'POST':
        team_form = TeamForm(request.POST)
        member_formset = MemberFormSet(request.POST)

        if team_form.is_valid() and member_formset.is_valid():
            # Create the team object in memory
            created_team = team_form.save(commit=False)
            # Manually add the leader's email (since it's not in the form)
            created_team.lead_email = user_email
            # Save the team to the database
            created_team.save()
            
            # Link the member formset to the new team and save
            member_formset.instance = created_team
            member_formset.save()

            # --- NEW: SEND CONFIRMATION EMAIL ---
            try:
                subject = 'Your Vogue Nation Registration is Confirmed!'
                message = f"""
                Hi {created_team.lead_name},

                Thank you for registering for Vogue Nation!

                Your team, "{created_team.team_name}", has been successfully registered for the {created_team.competition.competition_name} competition.

                We are excited to see what you bring to the runway.

                Best of luck,
                Vogue Nation,
                Alcheringa.
                """
                # This 'from_email' can be anything for the console backend
                from_email = 'noreply@voguenation.com'  
                recipient_list = [created_team.lead_email]

                send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            
            except Exception as e:
                # If email fails, print the error to the console but don't crash
                print(f"Error sending confirmation email: {e}")
            # --- END OF NEW EMAIL CODE ---

            return redirect('core:success')
    
    else:
        # --- GET request: Pre-fill the form ---
        initial_data = {
            'lead_name': request.user.get_full_name(),
        }

        # Check if a competition was stored in the session
        competition_name = request.session.get('selected_competition')
        if competition_name:
            try:
                # Find the competition object from the database
                competition_obj = Competition.objects.get(competition_name__iexact=competition_name)
                # Add it to the initial data for the form
                initial_data['competition'] = competition_obj
            except Competition.DoesNotExist:
                pass 
            
            # CRITICAL: Clear the session variable after using it
            if 'selected_competition' in request.session:
                del request.session['selected_competition']
        
        team_form = TeamForm(initial=initial_data)
        member_formset = MemberFormSet()

    context = {
        'team_form': team_form,
        'member_formset': member_formset,
        'leader_email': user_email, # Pass the email to the template
    }
    return render(request, 'core/registration/register.html', context)

def success_view(request):
    """
    Renders the success page after a successful registration.
    """
    return render(request, 'core/registration/success.html')

def register_for_competition_view(request, competition_name):
    """
    This view captures the competition choice from the URL,
    saves it in the session, and then starts the Google login flow.
    """
    # Store the competition name in the session
    request.session['selected_competition'] = competition_name
    
    # Redirect the user to the standard Google login URL
    # allauth will automatically handle the rest
    return redirect('/accounts/google/login/')