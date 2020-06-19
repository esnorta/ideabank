from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.contrib.auth.mixins import (LoginRequiredMixin,
     PermissionRequiredMixin)
from django.urls import reverse
from django.views import generic
from django.shortcuts import get_object_or_404
from groups.models import Group, GroupMembers
from . import models


class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'description')
    model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group

class JoinGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug = self.kwargs.get('slug'))

        try:
            GroupMembers.objects.create(user = self.request.user, group = group)
            # Try to get the GroupMember object and create one with user = user
            # and group = group
        except IntegrityError:
            messages.warning(self.request, 'Warning already a member!')
        else:
            messages.success(self.request, 'You are now a member!')

        return super().get(request, *args, **kwargs)

class LeaveGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        try:
            membership = models.GroupMembers.objects.filter(
                    user = self.request.user,
                    group__slug = self.kwargs.get('slug')
                ).get()
        except models.GroupMembers.DoesNotExist:
            messages.warning(self.request, "Sorry you aren't in this group!")
        else:
            membership.delete()
            messages.success(self.request, 'You have left the group')
        return super().get(request, *args, **kwargs)

