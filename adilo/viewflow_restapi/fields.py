from django.apps import apps
from django.db import models


def import_flow_by_ref(flow_strref):
    app_label, flow_path = flow_strref.split("/")
    app_config = apps.get_app_config(app_label)
    if not app_config:
        return None
    return app_config.module.__name__


class FlowReferenceField(models.TextField):

    pass


class TaskReferenceField(models.TextField):

    pass
