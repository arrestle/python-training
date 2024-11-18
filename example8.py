import random
import sys

from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton,
                               QVBoxLayout, QWidget)
from __feature__ import snake_case, true_property


class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.hello = [
            "Hallo Welt",
            "ä½ å¥½ï¼Œä¸–ç•Œ",
            "Hei maailma",
            "Hola Mundo",
            "ÐŸÑ€Ð¸Ð²ÐµÑ‚ Ð¼Ð¸Ñ€",
        ]

        self.button = QPushButton("Click me!")
        self.message = QLabel("Hello World")
        self.button.set_style_sheet("color: white; background-color: blue; margin: 10px; padding: 10px; border-radius: 5px;")
        self.message.alignment = Qt.AlignCenter
        self.message.set_style_sheet("color: white; background-color: green; margin: 10px; padding: 10px; border-radius: 5px;")  
       

        self.layout = QVBoxLayout(self)
        # make the layout large enough to accommodate the label and message comfortably
        # self.layout.set_contents_margins(100, 100, 100, 100)
        self.layout.add_widget(self.message)
        self.layout.add_widget(self.button)
        self.layout.set_alignment(self.message, Qt.AlignCenter)
        self.layout.set_alignment(self.button, Qt.AlignCenter)

        # Connecting the signal
        self.button.clicked.connect(self.magic)

    @Slot()
    def magic(self):
        self.message.text = random.choice(self.hello)
        # resize the label to fit the text
        self.message.adjust_size()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec())