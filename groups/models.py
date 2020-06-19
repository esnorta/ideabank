from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Allows to remove characters: if you have spaces, add dashes and bla bla

import misaka
# Import links, markdown

from django import template
register = template.Library()
# We can use custom template tags. In-group members templte tags

from django.contrib.auth import get_user_model
User = get_user_model()

class Group(models.Model):
    name = models.CharField(max_length = 255, unique = True)
    slug = models.SlugField(allow_unicode = True, unique = True)
    description = models.TextField(blank = True, default = '')
    description_html = models.TextField(editable = False, default='',
            blank = True)
    members = models.ManyToManyField(User, through = 'GroupMembers')

    def __str__(self):
        return self.name

    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        # Replacing and lowercasing things
        self.description_html = misaka.html(self.description)
        # Misaka gives markdown
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs = {'slug':self.slug})

    class Meta:
        ordering = ['name']

class GroupMembers(models.Model):
    group = models.ForeignKey(Group, related_name = 'memberships',
            on_delete = models.CASCADE)
    user = models.ForeignKey(User, related_name = 'user_groups',
            on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')
