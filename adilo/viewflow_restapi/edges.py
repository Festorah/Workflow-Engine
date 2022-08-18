from django.db.models import TextChoices


class Edge(object):
    """Each edge in the flowchart"""

    def __init__(self, src, dst, edge_class):
        """
        edge_class: next represents the next step directly
            cond_true: Represents true to execute
            cond_false: Represents false to execute
        """
        self._src = src
        self._dst = dst
        self._edge_class = edge_class

    @property
    def src(self):
        return self._src

    @property
    def dst(self):
        return self._dst

    @property
    def edge_class(self):
        return self._edge_class

    def __str__(self):
        return f"[{self.edge_class}] {self.src} ---> {self.dst}"


class STATUS_CHOICE(TextChoices):
    NEW = "NEW", "NEW"
    STARTED = "STARTED", "STARTED"
    DONE = "DONE", "DONE"
    CANCELED = "CANCELED", "CANCELED"
