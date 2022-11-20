# eventdetails.py
# Copyright 2022 Roger Marsh
# Licence: See LICENCE (BSD licence)

"""Set and modify event details."""
from chessvalidate import gui

from ..core import configuration


class EventDetails(gui.eventdetails.EventDetails):
    """Customise chessvalidate.gui.eventdetails for setting event details.

    Most of chessvalidate.gui.eventdetails.EventDetails is correct for
    chesstabular.

    ecfformat.gui.Header can be used 'as-is' but conventions such as field
    name styles and file storage options assume the target is always an ECF
    result submission file.

    """

    _RSF_EXT = ".conf"
    _RSF_PATTERN = "tabular" + _RSF_EXT

    def _make_configuration(self):
        """Return a configuration.Configuration instance."""
        return configuration.Configuration()
