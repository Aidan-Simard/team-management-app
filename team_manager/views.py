from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import AddForm
from .models import Member


class AddMemberView(View):
    """
    View for adding new members to the team.
    """

    form_class = AddForm
    template_name = "add_member.html"

    def get(self, request, *args, **kwargs):
        """
        Get request returns the template to add a new member.
        """
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        """
        Post request validates form information.

        If the information is valid, the db is updated
        and the user is redirected to the list page.

        Otherwise, keep the user on the current page and display errors.
        """
        form = self.form_class(request.POST)
        if form.is_valid():
            member = Member.objects.create(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                email=form.cleaned_data["email"],
                phone=form.cleaned_data["phone"],
                admin=form.cleaned_data["admin"],
            )
            member.save()

            return HttpResponseRedirect("/team/list/")

        return render(request, self.template_name, {"form": form})


class ListMembersView(View):
    """
    View for listing current team members.
    """

    template_name = "list_members.html"

    def get(self, request, *args, **kwargs):
        """
        Get request for viewing current team members.
        """
        members = Member.objects.all()
        return render(request, self.template_name, {"members": members})
