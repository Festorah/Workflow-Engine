from django.db import models
from viewflow_restapi.models import AbstractTask
from .hire_process import HireProcess  # noqa


class HireTask(AbstractTask):
    process = models.ForeignKey(
        HireProcess, related_name="tasks", on_delete=models.CASCADE)

    class Meta:
        verbose_name = verbose_name_plural = "HireTasks"

    def __str__(self):
        return "SingleHireTask {}, id: {}".format(self.flow_task, self.id)
