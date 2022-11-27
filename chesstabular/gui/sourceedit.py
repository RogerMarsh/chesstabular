# sourceedit.py
# Copyright 2008 Roger Marsh
# Licence: See LICENCE (BSD licence)

"""Schedule and results raw data edit class.

Add creation of tabular source documents to SourceEdit class.

"""

import tkinter
import tkinter.messagebox
import os
import csv

from chessvalidate.gui import sourceedit
from chessvalidate.core.gameobjects import (
    get_game_rows_for_csv_format,
)

from ..core import constants
from ..core import configuration


class SourceEdit(sourceedit.SourceEdit):
    """The Edit panel for raw results data."""

    _btn_tabular = "sourceedit_tabular"

    def describe_buttons(self):
        """Define all action buttons that may appear on data input page."""
        self.define_button(
            self._btn_generate,
            text="Generate",
            tooltip="Generate data for input to League database.",
            underline=0,
            command=self.on_generate,
        )
        self.define_button(
            self._btn_toggle_compare,
            text="Show Original",
            tooltip=" ".join(
                (
                    "Display original and edited results data but",
                    "not generated data.",
                )
            ),
            underline=5,
            command=self.on_toggle_compare,
        )
        self.define_button(
            self._btn_toggle_generate,
            text="Hide Original",
            tooltip=" ".join(
                (
                    "Display edited source and generated data but",
                    "not original source.",
                )
            ),
            underline=5,
            command=self.on_toggle_generate,
        )
        self.define_button(
            self._btn_save,
            text="Save",
            tooltip=(
                "Save edited results data with changes from original noted."
            ),
            underline=2,
            command=self.on_save,
        )
        self.define_button(
            self._btn_report,
            text="Report",
            tooltip="Save reports generated from source data.",
            underline=2,
            command=self.on_report,
        )
        self.define_button(
            self._btn_tabular,
            text="Tabular",
            tooltip="Save tabular version from source data.",
            underline=3,
            command=self.on_tabular,
        )
        self.define_button(
            self.btn_closedata,
            text="Close",
            tooltip="Close the folder containing data.",
            underline=0,
            switchpanel=True,
            command=self.on_close_data,
        )

    def on_tabular(self, event=None):
        """Create tabular version of source from validated source document."""
        del event
        if self.create_tabular_source():
            self.show_buttons_for_generate()
            self.create_buttons()

    def show_buttons_for_update(self):
        """Show buttons for actions allowed after generating reports."""
        self.hide_panel_buttons()
        self.show_panel_buttons(
            (
                self._btn_generate,
                self._btn_toggle_compare,
                self.btn_closedata,
                self._btn_save,
                self._btn_report,
                self._btn_tabular,
            )
        )

    def create_tabular_source(self):
        """Show create tabular source dialogue and return True if created."""
        if self.is_report_modified():
            tkinter.messagebox.showinfo(
                parent=self.get_widget(),
                message="".join(
                    (
                        "Event data has been modified.\n\n",
                        "Save the data first.",
                    )
                ),
                title="Create Tabular Source",
            )
            return False

        conf = configuration.Configuration()
        filename = tkinter.filedialog.asksaveasfilename(
            parent=self.get_widget(),
            title="Create Tabular Source",
            defaultextension=".csv",
            filetypes=(("Comma Separated Values (CSV) file", "*.csv"),),
            initialdir=conf.get_configuration_value(
                constants.RECENT_TABULAR_EVENTS
            ),
        )
        if not filename:
            tkinter.messagebox.showwarning(
                parent=self.get_widget(),
                title="Create Tabular Source",
                message="Tabular source file not saved",
            )
            return None
        conf.set_configuration_value(
            constants.RECENT_TABULAR_EVENTS,
            conf.convert_home_directory_to_tilde(os.path.dirname(filename)),
        )
        self._collate_unfinished_games()
        rows = sorted(
            get_game_rows_for_csv_format(
                self.get_context().results_data.get_collated_games()
            )
        )
        trro = {
            item: i
            for i, item in enumerate(constants.TABULAR_REPORT_ROW_ORDER)
        }
        trdso = constants.TABULAR_REPORT_DEFAULT_SOURCE_ORDER
        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=trdso)
            writer.writeheader()
            for row in rows:
                writer.writerow({item: row[trro[item]] for item in trdso})
        tkinter.messagebox.showinfo(
            parent=self.get_widget(),
            message="".join(
                (
                    "Tabular Source saved in\n\n",
                    filename,
                )
            ),
            title="Create Tabular Source",
        )
        return True
