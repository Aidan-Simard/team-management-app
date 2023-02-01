from django.urls import path
from team_manager.views import AddMemberView, ListMembersView, EditMemberView

urlpatterns = [
    path("add/", AddMemberView.as_view(), name="add"),
    path("list/", ListMembersView.as_view(), name="list"),
    path("edit/<int:id>", EditMemberView.as_view(), name="edit"),
]
