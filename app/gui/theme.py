# app/gui/theme.py


class AppColors:

    # =========================================================
    # Main
    # =========================================================

    BACKGROUND = "#00111C"

    PANEL = "#001A2C"

    HEADER = "#001523"

    CARD = "#181D24"

    # =========================================================
    # Button
    # =========================================================

    BUTTON = "#181D24"

    BUTTON_HOVER = "#006FAE"

    BUTTON_ACTIVE = "#0078B8"

    BUTTON_PRESSED = "#005A8C"

    # =========================================================
    # Border
    # =========================================================

    BORDER = "#313437"

    # =========================================================
    # Text
    # =========================================================

    TEXT_PRIMARY = "#FFFFFF"

    TEXT_SECONDARY = "#8B8B8B"

    TEXT_DISABLED = "#5D6870"

    # =========================================================
    # Accent
    # =========================================================

    ACCENT = "#1B156D"

    # =========================================================
    # Progress
    # =========================================================

    PROGRESS_BACKGROUND = "#E0E0E0"

    # =========================================================
    # Status
    # =========================================================

    SUCCESS = "#4CAF50"

    ERROR = "#D32F2F"


class AppTheme:

    @staticmethod
    def stylesheet():

        return f"""
        QWidget {{
            background-color: {AppColors.BACKGROUND};
            color: {AppColors.TEXT_PRIMARY};

            font-family: "Inria Serif";
            font-weight: bold;
            font-style: italic;
        }}

        QMainWindow {{
            background-color: {AppColors.BACKGROUND};
        }}

        QLabel {{
            color: {AppColors.TEXT_PRIMARY};

            font-family: "Inria Serif";
            font-weight: bold;
            font-style: italic;
        }}

        QPushButton {{
            background-color: {AppColors.BUTTON};

            border: 1px solid {AppColors.BORDER};
            border-radius: 6px;

            color: {AppColors.TEXT_PRIMARY};

            font-family: "Inria Serif";
            font-weight: bold;
            font-style: italic;
        }}

        QPushButton:hover {{
            background-color: {AppColors.BUTTON_HOVER};
        }}

        QPushButton:pressed {{
            background-color: {AppColors.BUTTON_PRESSED};
        }}

        QTextEdit {{
            background-color: {AppColors.CARD};

            border: 1px solid {AppColors.BORDER};
            border-radius: 8px;

            color: {AppColors.TEXT_PRIMARY};

            font-family: "Inria Serif";
            font-weight: bold;
            font-style: italic;
        }}

        QScrollBar:vertical {{
            background-color: {AppColors.CARD};

            width: 8px;

            border-radius: 4px;
        }}

        QScrollBar::handle:vertical {{
            background-color: {AppColors.TEXT_SECONDARY};

            border-radius: 4px;

            min-height: 30px;
        }}
        """