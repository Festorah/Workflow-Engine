import logging

from django.urls import include, path

from . import flows

log = logging.getLogger(__name__)


log.info("execute hire.urls.py")

flow = flows.HireFlow()

urls = flow.urls
log.info("finished")
log.info(f"urls: {urls}")


app_name = "hire"

urlpatterns = [
    path("hireflow/", include((urls, "hireflow"), namespace="hireflow")),
]
