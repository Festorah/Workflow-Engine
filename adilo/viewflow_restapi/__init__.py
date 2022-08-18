import logging

log = logging.getLogger(__name__)


class ThisObject(object):
    def __init__(self, name):
        self.name = name


class This(object):
    def __getattr__(self, name):
        return ThisObject(name)


this = This()
