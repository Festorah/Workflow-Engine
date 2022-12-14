import logging

from rest_framework import serializers
from rest_framework.generics import CreateAPIView, UpdateAPIView

from . import views

log = logging.getLogger(__name__)


def create_serializer(model, fields):
    all_fields = model._meta.get_fields()  # noqa: F841
    simple_fields = model._meta.fields  # noqa: F841

    class Serializer(serializers.ModelSerializer):
        class Meta:
            fields = []

    serializer_class = Serializer
    serializer_class.Meta.model = model
    serializer_class.Meta.fields = fields

    return serializer_class


class AutoSerializerMixin(object):
    def get_auto_serializer_class(self):
        task = self.kwargs["flow_task"]
        model = task.flow_class.process_class
        fields = task._view_args["fields"]
        return create_serializer(model, fields)

    def get_serializer_class(self):
        task = self.kwargs["flow_task"]
        serializer_class = task._view_args.get("serializer_class", None)
        if serializer_class is not None:
            return serializer_class
        return self.get_auto_serializer_class()


class AutoCreateAPIView(views.StartViewMixin, AutoSerializerMixin, CreateAPIView):
    """
    start = flows.Start(
        AutoCreateAPIView(
            model=HireProcess,
            fields=["name"],
        )
    )
    """


class AutoUpdateAPIView(views.UpdateViewMixin, AutoSerializerMixin, UpdateAPIView):
    """
    approve = flows.View(
        AutoUpdateAPIView(
            model=HireProcess,
            fields=["approved"],
        )
    )
    """
