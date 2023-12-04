from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import TeamMember
from .forms import TeamMemberForm

class TeamMemberListView(ListView):
    model = TeamMember
    context_object_name = 'team_members'
    template_name = 'team/team_member_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_team_members'] = TeamMember.objects.count()
        return context

class TeamMemberCreateView(CreateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'team/team_member_form.html'
    success_url = reverse_lazy('team:list')

class TeamMemberUpdateView(UpdateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'team/team_member_form.html'
    success_url = reverse_lazy('team:list')

class TeamMemberDeleteView(DeleteView):
    
    model = TeamMember
    context_object_name = 'team_member'
    template_name = 'team/team_member_confirm_delete.html'
    success_url = reverse_lazy('team:list')
