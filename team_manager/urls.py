from django.urls import path
from team_manager.views import AddMemberView, ListMembersView

urlpatterns = [
    path("add/", AddMemberView.as_view()),
    path("list/", ListMembersView.as_view()),
]
