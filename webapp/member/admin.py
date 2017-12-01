from django.contrib import admin
from . import models


class GenericAdmin(admin.ModelAdmin):
    prepopulated_fields = {'mobile_number': ('avatar', )}


# Register your models here.
admin.site.register(models.UserProfile, GenericAdmin)
