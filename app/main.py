import sys

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication

from gui.window import BanpedTranscriber


def main():
    app = QApplication(sys.argv)

    app.setApplicationName("Transcriber X")
    app.setApplicationDisplayName("Transcriber X")

    app.setFont(
        QFont("Inria Serif", 20)
    )

    window = BanpedTranscriber()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()