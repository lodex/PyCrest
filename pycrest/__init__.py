import logging


class NullHandler(logging.Handler):
    def emit(self, record):
        pass

logger = logging.getLogger('pycrest')
logger.addHandler(NullHandler())

client = 'PyCrest(lodex fork)'
version = "0.0.3.devel"

from .eve import EVE