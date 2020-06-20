from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Allows to remove characters: if you have spaces, add dashes and bla bla

from unidecode import unidecode
from django.template import defaultfilters


import misaka
# Import links, markdown

from django import template
register = template.Library()
# We can use custom template tags. In-group members templte tags
from django.core.validators import MaxValueValidator, MinValueValidator

from django.contrib.auth import get_user_model
User = get_user_model()

class Group(models.Model):
    name = models.CharField(max_length = 255, unique = True)
    slug = models.SlugField(allow_unicode = True, unique = True)
    description = models.TextField(blank = True, default = '')
    description_html = models.TextField(editable = False, default='',
            blank = True)
    members = models.ManyToManyField(User, through = 'GroupMembers')
    cost = models.FloatField(blank = True, null = True)
    eco = models.FloatField(blank = True, default = 0)
    importance = models.IntegerField(blank = True, null = True,
            validators=[MaxValueValidator(10), MinValueValidator(1)])
    complexity = models.IntegerField(blank = True, null = True,
            validators=[MaxValueValidator(10), MinValueValidator(1)])
    proj_time = models.FloatField(blank = True, null = True)

    def __str__(self):
        return self.name

    def save(self,*args, **kwargs):
        self.slug = defaultfilters.slugify(unidecode(self.name))
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
