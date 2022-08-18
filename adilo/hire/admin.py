from django.contrib import admin

from . import models


@admin.register(models.HireProcess)
class HireProcessAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "approved",
        "status",
        "create_datetime",
        "finish_datetime",
    ]


@admin.register(models.HireTask)
class HireTask(admin.ModelAdmin):
    list_display = [
        "id",
        "flow_task",
        "flow_task_type",
        "status",
        "create_datetime",
        "finish_datetime",
        "operator",
    ]


@admin.register(models.User)
class User(admin.ModelAdmin):
    list_display = ["id", "name"]
