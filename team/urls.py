from django.urls import path
from .views import TeamMemberListView, TeamMemberCreateView, TeamMemberUpdateView, TeamMemberDeleteView

app_name = 'team'  # This is the app_name that Django is expecting.

urlpatterns = [
    path('', TeamMemberListView.as_view(), name='list'),
    path('add/', TeamMemberCreateView.as_view(), name='add'),
    path('edit/<int:pk>/', TeamMemberUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', TeamMemberDeleteView.as_view(), name='delete'),

]