from django.forms import ModelForm
from .models import TeamMember

class TeamMemberForm(ModelForm):
    class Meta:
        model = TeamMember
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'role']
