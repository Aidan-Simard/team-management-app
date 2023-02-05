from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
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

            return redirect("/team/list/")

        return render(request, self.template_name, {"form": form})


class ListMembersView(ListView):
    """
    View for listing current team members.
    """

    template_name = "list_members.html"
    model = Member

    def get_context_data(self, **kwargs):
        """
        Get request renders the template to view current team members.
        """
        context = super().get_context_data(**kwargs)
        return context


class EditMemberView(DetailView):
    """
    View for editing a team member.
    """

    form_class = AddForm
    model = Member
    template_name = "add_member.html"
    slug_field = "id"

    def get_context_data(self, **kwargs):
        """
        Get request renders the template to edit a team member.
        """
        context = super().get_context_data(**kwargs)
        if "form" not in kwargs:
            context["form"] = self.form_class(
                initial={
                    "first_name": context["member"].first_name,
                    "last_name": context["member"].last_name,
                    "email": context["member"].email,
                    "phone": context["member"].phone,
                    "admin": context["member"].admin,
                }
            )
        else:
            context["form"] = kwargs["form"]

        return context

    def post(self, request, *args, **kwargs):
        """
        Post request updates the user information or deletes a user.
        """
        if "save" in request.POST:
            self.object = self.get_object()
            form = self.form_class(request.POST)
            if form.is_valid():
                Member.objects.filter(id=kwargs["pk"]).update(
                    first_name=form.cleaned_data["first_name"],
                    last_name=form.cleaned_data["last_name"],
                    email=form.cleaned_data["email"],
                    phone=form.cleaned_data["phone"],
                    admin=form.cleaned_data["admin"],
                )
                return redirect("/team/list/")

            # display errors
            return render(
                request,
                template_name=self.template_name,
                context=self.get_context_data(form=form),
            )

        elif "delete" in request.POST:
            Member.objects.get(id=kwargs["pk"]).delete()
            return redirect("/team/list/")

        return redirect(f"/team/edit/{kwargs['pk']}")
