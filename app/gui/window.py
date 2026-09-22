import os

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QStackedWidget,
    QLabel,
    QFileDialog,
    QScrollArea,
    QMessageBox,
    QPushButton,
)

from .widgets import (
    Header,
    PopupMenu,
    FileInformation,
    GradientProgressBar,
    ResultTextEdit,
    ActionButton,
)
from .theme import AppTheme
from datetime import datetime
from pathlib import Path

from ..services.history import History
from ..services.api_client import ApiClient



# ================================================================
# Home Page
# ================================================================

class HomePage(QWidget):

    def __init__(
        self,
        parent=None,
    ):
        super().__init__(parent)

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            20,
            20,
            20,
            15,
        )

        layout.setSpacing(10)

        # ---------------------------------------------------------
        # File Information
        # ---------------------------------------------------------

        self.file_information = FileInformation()

        layout.addWidget(
            self.file_information
        )

        # ---------------------------------------------------------
        # Progress
        # ---------------------------------------------------------

        self.progress_bar = GradientProgressBar()

        layout.addWidget(
            self.progress_bar
        )

        # ---------------------------------------------------------
        # Result
        # ---------------------------------------------------------

        self.result_text = ResultTextEdit()

        layout.addWidget(
            self.result_text,
            1,
        )

        # ---------------------------------------------------------
        # Buttons
        # ---------------------------------------------------------

        button_layout = QHBoxLayout()

        button_layout.setSpacing(
            8
        )

        self.select_button = ActionButton(
            "CHOOSE FILE"
        )

        self.save_button = ActionButton(
            "SAVE AS .TXT"
        )

        self.cancel_button = ActionButton(
            "CANCEL"
        )

        button_layout.addWidget(
            self.select_button
        )

        button_layout.addWidget(
            self.save_button
        )

        button_layout.addWidget(
            self.cancel_button
        )

        layout.addLayout(
            button_layout
        )

        # ---------------------------------------------------------
        # Connections
        # ---------------------------------------------------------

        self.select_button.clicked.connect(
            self.select_file
        )

        self.save_button.clicked.connect(
            self.save_result
        )

        self.cancel_button.clicked.connect(
            self.clear_all
        )

    # ============================================================
    # Select File
    # ============================================================

    def select_file(self):

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Audio File",
            "",
            (
                "Audio Files "
                "(*.mp3 *.wav *.m4a *.flac *.aac *.ogg *.mp4)"
                ";;All Files (*)"
            ),
        )

        if not file_path:
            return

        self.file_information.set_file(
            file_path
        )

    # ============================================================
    # Save Result
    # ============================================================

    def save_result(self):

        text = self.result_text.toPlainText()

        if not text.strip():
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Transcript",
            "transcript.txt",
            "Text Files (*.txt)",
        )

        if not file_path:
            return

        with open(
            file_path,
            "w",
            encoding="utf-8",
        ) as file:

            file.write(
                text
            )

    # ============================================================
    # Cancel
    # ============================================================

    def clear_all(self):

        self.file_information.clear()

        self.result_text.clear()

        self.progress_bar.setValue(
            0
        )


# ================================================================
# Account Page
# ================================================================

class AccountPage(QWidget):

    def __init__(
        self,
        parent=None,
    ):
        super().__init__(parent)

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            25,
            20,
            25,
            20,
        )

        layout.setSpacing(
            0
        )

        # ---------------------------------------------------------
        # Title
        # ---------------------------------------------------------

        title = QLabel(
            "ACCOUNT"
        )

        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        title.setStyleSheet(
            """
            QLabel {
                color: #FFFFFF;

                font-family: "Inria Serif";
                font-size: 20px;
                font-weight: bold;
            }
            """
        )

        layout.addWidget(
            title
        )

        # ---------------------------------------------------------
        # Profile
        # ---------------------------------------------------------

        profile_title = QLabel(
            "PROFILE"
        )

        profile_title.setStyleSheet(
            """
            QLabel {
                margin-top: 15px;

                color: #FFFFFF;

                font-family: "Inria Serif";
                font-size: 14px;
                font-weight: bold;
                font-style: italic;
            }
            """
        )

        layout.addWidget(
            profile_title
        )

        username = QLabel(
            "USERNAME : (not login yet)"
        )

        email = QLabel(
            "EMAIL : (xxxxxxxxxxxx.gmail.com)"
        )

        layout.addWidget(
            username
        )

        layout.addWidget(
            email
        )

        # ---------------------------------------------------------
        # Status
        # ---------------------------------------------------------

        status_title = QLabel(
            "STATUS"
        )

        status_title.setStyleSheet(
            """
            QLabel {
                margin-top: 20px;

                color: #FFFFFF;

                font-family: "Inria Serif";
                font-size: 14px;
                font-weight: bold;
                font-style: italic;
            }
            """
        )

        layout.addWidget(
            status_title
        )

        credit = QLabel(
            "Credit left : (300)"
        )

        expired = QLabel(
            "Expired : 13:00:00"
        )

        layout.addWidget(
            credit
        )

        layout.addWidget(
            expired
        )

        # ---------------------------------------------------------
        # Bottom
        # ---------------------------------------------------------

        layout.addStretch()

        logout = ActionButton(
            "LOG OUT"
        )

        logout.setFixedWidth(
            85
        )

        layout.addWidget(
            logout,
            alignment=Qt.AlignmentFlag.AlignHCenter,
        )

        change_password = QLabel(
            "Change Password"
        )

        change_password.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        change_password.setStyleSheet(
            """
            QLabel {
                color: #5D6870;

                font-family: "Inria Serif";
                font-size: 12px;
            }
            """
        )

        layout.addWidget(
            change_password
        )

        # ---------------------------------------------------------
        # General Text Style
        # ---------------------------------------------------------

        self.setStyleSheet(
            """
            QWidget {
                background-color: #00111C;
            }

            QLabel {
                color: #FFFFFF;

                font-family: "Inria Serif";
                font-size: 13px;
                font-weight: bold;
            }
            """
        )


# ================================================================
# History Page
# ================================================================

class HistoryPage(QWidget):

    def __init__(
        self,
        history_service,
        parent=None,
    ):
        super().__init__(parent)

        self.history_service = history_service

        self.setup_ui()

        self.load_history()

    def setup_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            15,
            15,
            15,
            15,
        )

        layout.setSpacing(
            8
        )

        # =====================================================
        # Title
        # =====================================================

        title = QLabel(
            "HISTORY"
        )

        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        title.setStyleSheet(
            """
            QLabel {
                background: transparent;

                font-family: "Inria Serif";
                font-size: 20px;

                font-weight: bold;
                font-style: italic;

                margin-bottom: 8px;
            }
            """
        )

        layout.addWidget(
            title
        )

        # =====================================================
        # Scroll Area
        # =====================================================

        self.scroll_area = QScrollArea()

        self.scroll_area.setWidgetResizable(
            True
        )

        self.scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )

        self.scroll_area.setStyleSheet(
            """
            QScrollArea {
                background: transparent;

                border: none;
            }
            """
        )

        self.history_container = QWidget()

        self.history_layout = QVBoxLayout(
            self.history_container
        )

        self.history_layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        self.history_layout.setSpacing(
            8
        )

        self.history_layout.addStretch()

        self.scroll_area.setWidget(
            self.history_container
        )

        layout.addWidget(
            self.scroll_area
        )

    # =========================================================
    # Load History
    # =========================================================

    def load_history(self):

        # Remove old items

        while self.history_layout.count() > 1:

            item = self.history_layout.takeAt(
                0
            )

            widget = item.widget()

            if widget:

                widget.deleteLater()

        history = self.history_service.get_all()

        if not history:

            empty_label = QLabel(
                "No transcription history"
            )

            empty_label.setAlignment(
                Qt.AlignmentFlag.AlignCenter
            )

            empty_label.setStyleSheet(
                """
                QLabel {
                    color: #8B8B8B;

                    font-family: "Inria Serif";
                    font-size: 13px;

                    font-weight: bold;
                    font-style: italic;
                }
                """
            )

            self.history_layout.insertWidget(
                0,
                empty_label
            )

            return

        # =====================================================
        # History Items
        # =====================================================

        for record in history:

            item = self.create_history_item(
                record
            )

            self.history_layout.insertWidget(
                self.history_layout.count() - 1,
                item,
            )

    # =========================================================
    # Create Item
    # =========================================================

    def create_history_item(
        self,
        record,
    ):

        item = QWidget()

        item.setFixedHeight(
            75
        )

        item.setStyleSheet(
            """
            QWidget {
                background-color: #001A2C;

                border: 1px solid #313437;

                border-radius: 8px;
            }
            """
        )

        layout = QVBoxLayout(
            item
        )

        layout.setContentsMargins(
            10,
            7,
            8,
            7,
        )

        layout.setSpacing(
            2
        )

        # -----------------------------------------------------
        # File Name
        # -----------------------------------------------------

        file_name = QLabel(
            f"FILE : {record.get('file_name', '')}"
        )

        file_name.setStyleSheet(
            """
            QLabel {
                background: transparent;

                border: none;

                font-family: "Inria Serif";
                font-size: 11px;

                font-weight: bold;
                font-style: italic;
            }
            """
        )

        layout.addWidget(
            file_name
        )

        # -----------------------------------------------------
        # Date
        # -----------------------------------------------------

        date_time = QLabel(
            f"DATE : {record.get('date_time', '')}"
        )

        date_time.setStyleSheet(
            """
            QLabel {
                background: transparent;

                border: none;

                color: #8B8B8B;

                font-family: "Inria Serif";
                font-size: 10px;

                font-weight: bold;
                font-style: italic;
            }
            """
        )

        layout.addWidget(
            date_time
        )

        # -----------------------------------------------------
        # Download
        # -----------------------------------------------------

        download_button = QPushButton(
            "DOWNLOAD"
        )

        download_button.setFixedSize(
            85,
            25
        )

        download_button.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        download_button.setStyleSheet(
            """
            QPushButton {
                background-color: #181D24;

                border: 1px solid #313437;

                border-radius: 5px;

                color: #FFFFFF;

                font-family: "Inria Serif";
                font-size: 10px;

                font-weight: bold;
                font-style: italic;
            }

            QPushButton:hover {
                background-color: #006FAE;
            }
            """
        )

        download_button.clicked.connect(
            lambda checked=False,
            current_record=record:
            self.download_record(
                current_record
            )
        )

        layout.addWidget(
            download_button,
            alignment=Qt.AlignmentFlag.AlignRight,
        )

        return item

    # =========================================================
    # Download History
    # =========================================================

    def download_record(
        self,
        record,
    ):

        file_name = record.get(
            "file_name",
            "transcript",
        )

        transcript = record.get(
            "transcript",
            "",
        )

        default_name = (
            Path(file_name).stem
            + "_transcript.txt"
        )

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Download Transcript",
            default_name,
            "Text Files (*.txt)",
        )

        if not file_path:

            return

        try:

            with open(
                file_path,
                "w",
                encoding="utf-8",
            ) as file:

                file.write(
                    transcript
                )

        except OSError as error:

            QMessageBox.critical(
                self,
                "Download Error",
                str(error),
            )

# ================================================================
# About Page
# ================================================================

class AboutPage(QWidget):

    def __init__(
        self,
        parent=None,
    ):
        super().__init__(parent)

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            25,
            20,
            25,
            15,
        )

        layout.setSpacing(
            5
        )

        # ---------------------------------------------------------
        # Spacer
        # ---------------------------------------------------------

        layout.addStretch()

        # ---------------------------------------------------------
        # Logo
        # ---------------------------------------------------------

        logo = QLabel()

        logo_path = os.path.join(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(
                        os.path.abspath(__file__)
                    )
                )
            ),
            "assets",
            "logo.png",
        )

        if os.path.exists(
            logo_path
        ):

            logo.setPixmap(
                QIcon(
                    logo_path
                ).pixmap(
                    55,
                    55,
                )
            )

        logo.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(
            logo
        )

        # ---------------------------------------------------------
        # Transcriber X
        # ---------------------------------------------------------

        title = QLabel(
            "TRANSCRIBER X"
        )

        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(
            title
        )

        subtitle = QLabel(
            "AI-Powered Audio Transcription"
        )

        subtitle.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(
            subtitle
        )

        version = QLabel(
            "Version 1.0.0"
        )

        version.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(
            version
        )

        description = QLabel(
            "Transcribe your audio quickly and accurately "
            "using AI-powered speech recognition."
        )

        description.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        description.setWordWrap(
            True
        )

        layout.addWidget(
            description
        )

        # ---------------------------------------------------------
        # Bottom Information
        # ---------------------------------------------------------

        layout.addStretch()

        developer = QLabel(
            "Developed by Banped"
        )

        developer.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(
            developer
        )

        copyright_text = QLabel(
            "© 2026 BANPED"
        )

        copyright_text.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(
            copyright_text
        )

        # ---------------------------------------------------------
        # Style
        # ---------------------------------------------------------

        self.setStyleSheet(
            """
            QWidget {
                background-color: #00111C;
            }

            QLabel {
                background-color: transparent;

                border: none;

                color: #FFFFFF;

                font-family: "Inria Serif";
                font-weight: bold;
            }
            """
        )


# ================================================================
# Main Window
# ================================================================

class BanpedTranscriber(QMainWindow):

    def __init__(self):

        super().__init__()

        # ---------------------------------------------------------
        # Window
        # ---------------------------------------------------------

        self.setWindowTitle(
            "Transcriber X"
        )

        self.setFixedSize(
            500,
            800,
        )

        # ---------------------------------------------------------
        # Logo
        # ---------------------------------------------------------

        logo_path = os.path.join(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(
                        os.path.abspath(__file__)
                    )
                )
            ),
            "assets",
            "logo.png",
        )

        if os.path.exists(
            logo_path
        ):

            self.setWindowIcon(
                QIcon(
                    logo_path
                )
            )

        # ---------------------------------------------------------
        # UI
        # ---------------------------------------------------------

        self.setup_ui()

    # ============================================================
    # Setup UI
    # ============================================================

    def setup_ui(self):

        central_widget = QWidget()

        self.setCentralWidget(
            central_widget
        )

        # ---------------------------------------------------------
        # Main Layout
        # ---------------------------------------------------------

        main_layout = QVBoxLayout(
            central_widget
        )

        main_layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        main_layout.setSpacing(
            0
        )

        # ---------------------------------------------------------
        # Header
        # ---------------------------------------------------------

        self.header = Header(
            "Transcriber X"
        )

        main_layout.addWidget(
            self.header
        )

        # ---------------------------------------------------------
        # Pages
        # ---------------------------------------------------------

        self.pages = QStackedWidget()

        self.home_page = HomePage()

        self.account_page = AccountPage()

        self.history_page = HistoryPage()

        self.about_page = AboutPage()

        self.pages.addWidget(
            self.home_page
        )

        self.pages.addWidget(
            self.account_page
        )

        self.pages.addWidget(
            self.history_page
        )

        self.pages.addWidget(
            self.about_page
        )

        main_layout.addWidget(
            self.pages
        )

        # ---------------------------------------------------------
        # Popup Menu
        # ---------------------------------------------------------

        self.popup_menu = PopupMenu(
            central_widget
        )

        self.popup_menu.move(
            0,
            40,
        )

        self.popup_menu.raise_()

        self.popup_menu.hide()

        # ---------------------------------------------------------
        # Header Menu
        # ---------------------------------------------------------

        self.header.menu_clicked.connect(
            self.toggle_menu
        )

        # ---------------------------------------------------------
        # Menu Navigation
        # ---------------------------------------------------------

        self.popup_menu.home_clicked.connect(
            self.show_home
        )

        self.popup_menu.account_clicked.connect(
            self.show_account
        )

        self.popup_menu.history_clicked.connect(
            self.show_history
        )

        self.popup_menu.about_clicked.connect(
            self.show_about
        )

        # ---------------------------------------------------------
        # Start Home
        # ---------------------------------------------------------

        self.show_home()

    # ============================================================
    # Toggle Menu
    # ============================================================

    def toggle_menu(self):

        if self.popup_menu.isVisible():

            self.popup_menu.hide()

        else:

            self.popup_menu.raise_()

            self.popup_menu.show()

    # ============================================================
    # Close Menu
    # ============================================================

    def close_menu(self):

        self.popup_menu.hide()

    # ============================================================
    # Home
    # ============================================================

    def show_home(self):

        self.pages.setCurrentWidget(
            self.home_page
        )

        self.popup_menu.set_active(
            "home"
        )

        self.close_menu()

    # ============================================================
    # Account
    # ============================================================

    def show_account(self):

        self.pages.setCurrentWidget(
            self.account_page
        )

        self.popup_menu.set_active(
            "account"
        )

        self.close_menu()

    # ============================================================
    # History
    # ============================================================

    def show_history(self):

        self.pages.setCurrentWidget(
            self.history_page
        )

        self.popup_menu.set_active(
            "history"
        )

        self.close_menu()

    # ============================================================
    # About
    # ============================================================

    def show_about(self):

        self.pages.setCurrentWidget(
            self.about_page
        )

        self.popup_menu.set_active(
            "about"
        )

        self.close_menu()