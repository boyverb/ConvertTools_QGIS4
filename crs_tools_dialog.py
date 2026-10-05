# -*- coding: utf-8 -*-
import os

# qgis.PyQt tự chọn PyQt5 (QGIS 3) hoặc PyQt6 (QGIS 4)
from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'crs_tools_dialog_base.ui'))


class CRSToolsDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
