import os

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont, QPainter, QLinearGradient
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QTextEdit,
    QProgressBar,
)

# ================================================================
# Color
# ================================================================
APPS_COLORS = {
    "bg_main": "#00111C", #พื้นหลัง
    "bg_panel": "#001A2C", #พื้นหลังแถบเมนู
    "bg_card": "#181D24", #การ์ด
    "bg_hover": "#006FAE", #สีhover
}

# ================================================================
# Font
# ================================================================

def create_inria_serif_font(
    size=20,
    bold=True,
    italic=False,
):
    font = QFont("Inria Serif")

    font.setPointSize(size)
    font.setBold(bold)
    font.setItalic(italic)

    return font


# ================================================================
# Header
# ================================================================

class Header(QWidget):

    menu_clicked = pyqtSignal()

    def __init__(
        self,
        title="Transcriber X",
        parent=None,
    ):
        super().__init__(parent)

        self.setup_ui(title)

    def setup_ui(self, title):

        self.setFixedHeight(40)

        layout = QHBoxLayout(self)

        layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        layout.setSpacing(0)

        # ---------------------------------------------------------
        # Hamburger
        # ---------------------------------------------------------

        self.menu_button = QPushButton("☰")

        self.menu_button.setFixedSize(
            40,
            40,
        )

        self.menu_button.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        self.menu_button.clicked.connect(
            self.menu_clicked.emit
        )

        layout.addWidget(
            self.menu_button
        )

        # ---------------------------------------------------------
        # Title
        # ---------------------------------------------------------

        self.title_label = QLabel(title)

        self.title_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(
            self.title_label,
            1,
        )

        # ---------------------------------------------------------
        # Empty space
        # ---------------------------------------------------------

        self.right_space = QWidget()

        self.right_space.setFixedWidth(
            40
        )

        layout.addWidget(
            self.right_space
        )

        # ---------------------------------------------------------
        # Style
        # ---------------------------------------------------------

        self.setStyleSheet(
            """
            Header {
                background-color: #001523;
            }

            QLabel {
                background-color: transparent;

                color: #FFFFFF;

                font-family: "Inria Serif";
                font-size: 20px;
                font-weight: bold;
            }

            QPushButton {
                background-color: transparent;

                border: none;

                color: #FFFFFF;

                font-family: "Inria Serif";
                font-size: 16px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #002033;
            }

            QPushButton:pressed {
                background-color: #00304A;
            }
            """
        )


# ================================================================
# Popup Menu
# ================================================================

class PopupMenu(QWidget):

    home_clicked = pyqtSignal()
    account_clicked = pyqtSignal()
    history_clicked = pyqtSignal()
    about_clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedSize(
            215,
            175,
        )

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        layout.setSpacing(0)

        # ---------------------------------------------------------
        # Home
        # ---------------------------------------------------------

        self.home_button = QPushButton(
            "HOME"
        )

        self.home_button.setFixedHeight(
            43
        )

        self.home_button.clicked.connect(
            self.home_clicked.emit
        )

        layout.addWidget(
            self.home_button
        )

        # ---------------------------------------------------------
        # Account
        # ---------------------------------------------------------

        self.account_button = QPushButton(
            "ACCOUNT"
        )

        self.account_button.setFixedHeight(
            43
        )

        self.account_button.clicked.connect(
            self.account_clicked.emit
        )

        layout.addWidget(
            self.account_button
        )

        # ---------------------------------------------------------
        # History
        # ---------------------------------------------------------

        self.history_button = QPushButton(
            "HISTORY"
        )

        self.history_button.setFixedHeight(
            43
        )

        self.history_button.clicked.connect(
            self.history_clicked.emit
        )

        layout.addWidget(
            self.history_button
        )

        # ---------------------------------------------------------
        # About
        # ---------------------------------------------------------

        self.about_button = QPushButton(
            "ABOUT"
        )

        self.about_button.setFixedHeight(
            43
        )

        self.about_button.clicked.connect(
            self.about_clicked.emit
        )

        layout.addWidget(
            self.about_button
        )

        # ---------------------------------------------------------
        # Style
        # ---------------------------------------------------------

        self.setStyleSheet(
            """
            PopupMenu {
                background-color: #001A2C;

                border: none;
            }

            QPushButton {
                background-color: #001A2C;

                border: none;

                color: #FFFFFF;

                font-family: "Inria Serif";
                font-size: 16px;
                font-weight: bold;

                text-align: left;

                padding-left: 35px;
            }

            QPushButton:hover {
                background-color: #006FAE;
            }

            QPushButton:pressed {
                background-color: #005A8C;
            }
            """
        )

    # ============================================================
    # Active Page
    # ============================================================

    def set_active(
        self,
        page,
    ):

        buttons = {
            "home": self.home_button,
            "account": self.account_button,
            "history": self.history_button,
            "about": self.about_button,
        }

        # Reset
        for button in buttons.values():

            button.setStyleSheet(
                """
                QPushButton {
                    background-color: #001A2C;
                    border: none;

                    color: #FFFFFF;

                    font-family: "Inria Serif";
                    font-size: 16px;
                    font-weight: bold;

                    text-align: left;

                    padding-left: 35px;
                }

                QPushButton:hover {
                    background-color: #006FAE;
                }
                """
            )

        # Active
        if page in buttons:

            buttons[page].setStyleSheet(
                """
                QPushButton {
                    background-color: #0078B8;
                    border: none;

                    color: #FFFFFF;

                    font-family: "Inria Serif";
                    font-size: 16px;
                    font-weight: bold;

                    text-align: left;

                    padding-left: 35px;
                }
                """
            )


# ================================================================
# File Information
# ================================================================

class FileInformation(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        layout.setSpacing(2)

        # ---------------------------------------------------------
        # File Name
        # ---------------------------------------------------------

        self.file_name_label = QLabel(
            "FILE NAME :"
        )

        # ---------------------------------------------------------
        # File Information
        # ---------------------------------------------------------

        self.file_type_label = QLabel(
            "FILE INFORMATION :"
        )

        # ---------------------------------------------------------
        # Status
        # ---------------------------------------------------------

        self.file_status_label = QLabel(
            "No file selected"
        )

        self.file_status_label.setMinimumHeight(
            30
        )

        layout.addWidget(
            self.file_name_label
        )

        layout.addWidget(
            self.file_type_label
        )

        layout.addWidget(
            self.file_status_label
        )

        # ---------------------------------------------------------
        # Style
        # ---------------------------------------------------------

        self.setStyleSheet(
            """
            QLabel {
                background-color: transparent;

                color: #FFFFFF;

                font-family: "Inria Serif";
                font-size: 15px;
                font-weight: bold;
            }

            QLabel:last-child {
                background-color: #181D24;

                border: 1px solid #313437;
                border-radius: 8px;

                padding: 5px 10px;
            }
            """
        )

    # ============================================================
    # Set File
    # ============================================================

    def set_file(
        self,
        file_path,
    ):

        file_name = os.path.basename(
            file_path
        )

        file_extension = os.path.splitext(
            file_path
        )[1]

        if file_extension:

            file_type = (
                file_extension
                .replace(".", "")
                .upper()
            )

        else:

            file_type = "UNKNOWN"

        self.file_name_label.setText(
            f"FILE NAME : {file_name}"
        )

        self.file_type_label.setText(
            f"FILE INFORMATION : {file_type}"
        )

        self.file_status_label.setText(
            file_path
        )

    # ============================================================
    # Clear
    # ============================================================

    def clear(self):

        self.file_name_label.setText(
            "FILE NAME :"
        )

        self.file_type_label.setText(
            "FILE INFORMATION :"
        )

        self.file_status_label.setText(
            "No file selected"
        )


# ================================================================
# Gradient Progress Bar
# ================================================================

class GradientProgressBar(QProgressBar):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setRange(
            0,
            100,
        )

        self.setValue(
            0
        )

        self.setTextVisible(
            True
        )

        self.setFixedHeight(
            20
        )

        self.setStyleSheet(
            """
            QProgressBar {
                background-color: #E0E0E0;

                border: none;
                border-radius: 10px;

                color: #000000;

                font-family: "Inria Serif";
                font-size: 11px;
                font-weight: bold;

                text-align: center;
            }

            QProgressBar::chunk {
                background-color: #1B156D;

                border-radius: 10px;
            }
            """
        )


# ================================================================
# Result Text
# ================================================================

class ResultTextEdit(QTextEdit):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setPlaceholderText(
            "Transcription result..."
        )

        self.setStyleSheet(
            """
            QTextEdit {
                background-color: #181D24;

                border: 1px solid #313437;
                border-radius: 8px;

                color: #FFFFFF;

                padding: 10px;

                font-family: "Inria Serif";
                font-size: 13px;
                font-weight: bold;
            }

            QScrollBar:vertical {
                background-color: #2A2D31;

                width: 8px;

                border-radius: 4px;
            }

            QScrollBar::handle:vertical {
                background-color: #8B8B8B;

                border-radius: 4px;

                min-height: 30px;
            }
            """
        )


# ================================================================
# Action Button
# ================================================================

class ActionButton(QPushButton):

    def __init__(
        self,
        text,
        parent=None,
    ):
        super().__init__(
            text,
            parent,
        )

        self.setFixedHeight(
            35
        )

        self.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        self.setStyleSheet(
            """
            QPushButton {
                background-color: #181D24;

                border: 1px solid #313437;
                border-radius: 6px;

                color: #FFFFFF;

                font-family: "Inria Serif";
                font-size: 13px;
                font-weight: bold;

                padding-left: 10px;
                padding-right: 10px;
            }

            QPushButton:hover {
                background-color: #252B33;
            }

            QPushButton:pressed {
                background-color: #303740;
            }
            """
        )