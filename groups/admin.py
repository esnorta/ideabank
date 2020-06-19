from django.contrib import admin
from . import models
# Register your models here.

class GroupMemberInline(admin.TabularInline):
    # Admin can change group members in admin panel
    model = models.GroupMembers


admin.site.register(models.Group)
