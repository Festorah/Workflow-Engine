import logging
from collections import defaultdict

from . import This, ThisObject
from .nodes import Node

log = logging.getLogger(__name__)


log.debug("Introduce viewflow_restapi.flows.py")


class _Resolver(object):
    def __init__(self, nodes):
        self.nodes = nodes

    def get_implementation(self, link):
        if isinstance(link, Node):
            node = link
        elif isinstance(link, ThisObject):
            node = self.nodes.get(link.name)
        elif isinstance(link, str):
            node = self.nodes.get(link)
        else:
            raise Exception(f"can not recognize {link}")
        if node:
            return node
        raise Exception(
            (
                f"no suitable node for {link}, "
                f"maybe there is a typo in you "
                f"flow_task: {getattr(link, 'name', 'unknown')}"
            )
        )


class FlowMeta(object):
    def __init__(self, app_label, flow_class, nodes):
        self.app_label = app_label
        self.flow_class = flow_class
        self._nodes_by_name = nodes

    def nodes(self):
        return self._nodes_by_name.values()


class FlowMetaClass(type):

    """
    the FlowMetaClass can generate the node relations according to the attrs of
    a Flow Class
    """

    def __new__(cls, class_name, bases, attrs, **kwargs):  # noqa: C901
        log.debug("creating a new Flow class")
        log.debug(attrs)
        new_class = super(FlowMetaClass, cls).__new__(cls, class_name, bases, attrs)

        nodes = {}
        # Initialize nodes according to the properties of Flow
        for name, attr in attrs.items():
            if isinstance(attr, Node):
                nodes[name] = attr

        # Set the name of the node
        for name, node in nodes.items():
            node.name = name

        resolver = _Resolver(nodes)
        for node in nodes.values():
            node._resolve(resolver)

        # Set the node's _incoming_edges
        # The node whose key is outgoing
        incoming = defaultdict(list)
        # A ---e---> B
        # e.src = A;  e.dst = B
        # incoming = {B: [e]}
        for _, node in nodes.items():
            for outgoing_edge in node._outgoing():
                incoming[outgoing_edge.dst].append(outgoing_edge)
        for node, edges in incoming.items():
            node._incoming_edges = edges

        for name, node in nodes.items():
            node.flow_class = new_class

        app_label = None
        new_class._meta = FlowMeta(app_label, new_class, nodes)
        for name, node in nodes.items():
            node.flow_class = new_class

        for name, node in nodes.items():
            node.ready()

        process_class = attrs.get("process_class", None)
        if process_class:
            if not hasattr(process_class, "registered_flows"):
                setattr(process_class, "registered_flows", set())
            process_class.registered_flows.add(new_class)
        return new_class


class Flow(metaclass=FlowMetaClass):

    process_class = None
    task_class = None
    process_title = None

    @property
    def urls(self):
        log.debug("Load Flow.urls")
        node_urls = []
        for node in self._meta.nodes():
            node_urls += node.urls()
        result = node_urls
        log.debug("Finish loading Flow.urls")
        log.debug(result)
        return result

    def __str__(self):
        return str(self.process_title)


this = This()
