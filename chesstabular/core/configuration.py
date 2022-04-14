# configuration.py
# Copyright 2022 Roger Marsh
# Licence: See LICENCE (BSD licence)

# This module is a canditate for a move to the solentware_misc package.
"""Access and update names of last used configuration files.

The initial values are taken from file named in self._RESULTS_CONF in the
user's home directory if the file exists.

"""

import os

from chessvalidate.core import configuration

from ..core import constants


class Configuration(configuration.Configuration):
    """Identify configuration file and access and update item values."""

    _RESULTS_CONF = ".chesstabular.conf"
    _DEFAULT_RECENTS = (
        (constants.RECENT_EMAIL_SELECTION, "~"),
        (constants.RECENT_EMAIL_EXTRACTION, "~"),
        (constants.RECENT_DOCUMENT, "~"),
        (constants.RECENT_TABULAR_EVENTS, "~"),
    )
