from django.db import models
from viewflow_restapi.models import AbstractProcess


class HireProcess(AbstractProcess):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
    name = models.CharField("name", max_length=31)
    gender = models.CharField("gender", choices=GENDER_CHOICES, max_length=10)
    approved = models.BooleanField(null=True, blank=True)
    salary = models.DecimalField(
        "salary",
        max_digits=9,
        decimal_places=2,
        null=True, blank=True)
    notified = models.BooleanField("notified", blank=True, default=False)
    background_ok = models.BooleanField("background ok", blank=True, null=True)

    class Meta:
        verbose_name = verbose_name_plural = "HireProcesses"

    def __str__(self):
        return "SingleHireProcess {}, id: {}".format(self.name, self.id)

