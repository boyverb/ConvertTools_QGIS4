# -*- coding: utf-8 -*-
import os

# qgis.PyQt tự chọn PyQt5 (QGIS 3) hoặc PyQt6 (QGIS 4)
from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'convertVN2000_DialogBase.ui'))


class ConvertVN2000Dialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # Hàm kiểm tra do plugin gán vào: trả về (tiêu đề, nội dung lỗi)
        # hoặc None nếu dữ liệu hợp lệ
        self.validator = None

    def accept(self):
        """Chỉ đóng hộp thoại khi dữ liệu nhập đã đầy đủ."""
        if self.validator is not None:
            problem = self.validator()
            if problem:
                title, text = problem
                QtWidgets.QMessageBox.warning(self, title, text)
                return  # giữ hộp thoại mở
        super().accept()
