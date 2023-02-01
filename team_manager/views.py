from django.shortcuts import render, redirect
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
        Get request renders the template to add a new member.
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
        Get request renders the template to view current team members.
        """
        members = Member.objects.all()
        return render(request, self.template_name, {"members": members})


class EditMemberView(View):
    """
    View for editing a team member.
    """

    form_class = AddForm
    template_name = "add_member.html"

    def get(self, request, *args, **kwargs):
        """
        Get request renders the template to edit a team member.
        """

        member = Member.objects.get(id=kwargs["id"])
        form = self.form_class(
            initial={
                "first_name": member.first_name,
                "last_name": member.last_name,
                "email": member.email,
                "phone": member.phone,
                "admin": member.admin,
            }
        )

        return render(request, self.template_name, {"member": member, "form": form})

    def post(self, request, *args, **kwargs):
        """
        Post request updates the user information or deletes a user.
        """

        if "save" in request.POST:
            form = self.form_class(request.POST)
            if form.is_valid():
                member = Member.objects.filter(id=kwargs["id"]).update(
                    first_name=form.cleaned_data["first_name"],
                    last_name=form.cleaned_data["last_name"],
                    email=form.cleaned_data["email"],
                    phone=form.cleaned_data["phone"],
                    admin=form.cleaned_data["admin"],
                )
                return HttpResponseRedirect("/team/list/")

            return redirect("/team/edit/", id=kwargs["id"])

        elif "delete" in request.POST:
            member = Member.objects.get(id=kwargs["id"]).delete()
            return HttpResponseRedirect("/team/list/")

        return redirect("/team/edit/", id=kwargs["id"])
