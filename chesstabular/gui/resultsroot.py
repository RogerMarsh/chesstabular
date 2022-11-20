# resultsroot.py
# Copyright 2010 Roger Marsh
# Licence: See LICENCE (BSD licence)

"""Results tabular application."""

from solentware_bind.gui.exceptionhandler import ExceptionHandler

import chessvalidate.gui.resultsroot

from .. import APPLICATION_NAME
from . import help_

# This statement gets a protected-access message from pylint.
# Cannot set by set_application_name() because chessvalidate.gui.resultsroot
# has already done a call to this method.
# ExceptionHandler.set_application_name(APPLICATION_NAME)
ExceptionHandler._application_name = APPLICATION_NAME


class Results(chessvalidate.gui.resultsroot.Results):
    """Results application."""

    def help_about(self):
        """Display information about Tabular Results application."""
        help_.help_about(self.root)

    def help_guide(self):
        """Display brief User Guide for Tabular Results application."""
        help_.help_guide(self.root)

    def help_keyboard(self):
        """Display list of keyboard actions for Tabular Results application."""
        help_.help_keyboard(self.root)
