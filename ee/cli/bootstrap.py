"""EasyEngine bootstrapping."""

# All built-in application controllers should be imported, and registered
# in this file in the same way as EEBaseController.

from cement.core import handler
from ee.cli.controllers.base import EEBaseController
from ee.cli.controllers.site import EESiteController
from ee.cli.controllers.stack import EEStackController
from ee.cli.controllers.debug import EEDebugController
from ee.cli.controllers.clean import EECleanController

def load(app):
    handler.register(EEBaseController)
    handler.register(EESiteController)
    handler.register(EEStackController)
    handler.register(EEDebugController)
    handler.register(EECleanController)
