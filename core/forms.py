from django import forms
from django.forms import inlineformset_factory
from .models import Team, Member_Detail, Competition

# --- Updated style for text/email/number inputs ---
# This style uses your new padding, border, and background
input_style = (
    "w-full p-4 bg-white/20 text-white self-stretch text-white/60 font-['Lorenza'] text-base not-italic font-normal leading-4"
    # "focus:outline-none focus:ring-2 focus:ring-blue-500"
)

# --- Updated style for <select> dropdowns ---
# I've matched the padding and border, but kept bg-black for readability
select_style = (
    "w-full p-4 bg-black text-white self-stretch text-white/60 font-['Lorenza'] text-base not-italic font-normal leading-4 border border-white"
)


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            'team_name',
            'competition',
            'prev_performance',
            'lead_name',
            'lead_gender',
            'lead_phone',
            'lead_city',
            'lead_postal_code',
        ]

        widgets = {
            'team_name': forms.TextInput(attrs={
                'placeholder': 'Enter Team Name',
                'class': input_style
            }),
            'competition': forms.RadioSelect(attrs={
                'class': 'hidden peer'
            }),
            'prev_performance': forms.TextInput(attrs={
                'placeholder': 'Enter Link Here',
                'class': input_style
            }),
            'lead_name': forms.TextInput(attrs={
                'placeholder': 'Full Name of Team Leader',
                'class': input_style
            }),
            'lead_gender': forms.Select(attrs={
                'class': select_style
            }),
            'lead_phone': forms.TextInput(attrs={
                'placeholder': 'Type Here',
                'class': "w-full p-4 bg-white/20 text-white self-stretch text-white/60 font-['Lorenza'] text-base not-italic font-normal leading-4"
            }),
            'lead_city': forms.TextInput(attrs={
                'placeholder': 'Type Here',
                'class': input_style
            }),
            'lead_postal_code': forms.NumberInput(attrs={
                'placeholder': 'Type Here',
                'class': input_style
            }),
        }


class MemberDetailForm(forms.ModelForm):
    class Meta:
        model = Member_Detail
        fields = [
            'name',
            'email',
            'phone_number',
            'your_city',
            'gender',
            'Postal_code',
        ]
        
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Type Here',
                'class': input_style
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Type Here',
                'class': input_style
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Type Here',
                'class': input_style
            }),
            'your_city': forms.TextInput(attrs={
                'placeholder': 'Type Here',
                'class': input_style
            }),
            'gender': forms.Select(attrs={
                'class': select_style
            }),
            'Postal_code': forms.NumberInput(attrs={
                'placeholder': 'Type Here',
                'class': input_style
            }),
        }


# This creates the formset for adding multiple members
MemberFormSet = inlineformset_factory(
    Team,
    Member_Detail,
    form=MemberDetailForm,
    extra=1,
    can_delete=True,
    can_delete_extra=True,
)