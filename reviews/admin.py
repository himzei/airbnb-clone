from django.contrib import admin
from . import models


@admin.register(models.Review)
class ReveiwAdmin(admin.ModelAdmin):

    list_display = ("__str__", "rating_average")

    pass
