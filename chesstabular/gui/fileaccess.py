# fileaccess.py
# Copyright 2022 Roger Marsh
# Licence: See LICENCE (BSD licence)

"""Provide open mailbox and configuration file methods for Tabular Results.

The chesstabular.core.configuration module is used rather than the one in
chessvalidate.core which is provided by the superclasses of SelectEmail
and Configure.

Module introduced in response to pylint duplicate-code message, and the
class is added to the ignored-classes list in pylint.conf to stop the
no-member error messages which replace the duplicate-code refactor message.
"""

from ..core import configuration


class FileAccess:
    """Define methods shared by SelectEmail and Configure classes."""

    def file_new(self, conf=configuration, recent=None):
        """Set configuration if None then delegate."""
        super().file_new(conf=conf, recent=recent)

    def file_open(self, conf=configuration, recent=None):
        """Set configuration if None then delegate."""
        super().file_open(conf=conf, recent=recent)
