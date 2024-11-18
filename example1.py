import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import Slot, Qt, Signal

# Initialize counter
counter = 0

# Greetings
@Slot()
def say_hello():
    global counter
    counter += 1
    print(f"Button clicked, Hello! {counter}")
    label.setText(f"<font color=red size=40>Hello World!</font> <font color=green size=40>{counter}</font>")

app = QApplication(sys.argv)


# Create a main window widget
main_window = QWidget()
main_window.setWindowTitle("Main Window")

# Create a layout
layout = QVBoxLayout()

# Create a label
label = QLabel("<font color=red size=40>Hello World!</font>")
layout.addWidget(label)

# Create a button
button = QPushButton("Click me")
button.clicked.connect(say_hello)
layout.addWidget(button)

# Create an exit button
exit_button = QPushButton("Exit")
exit_button.clicked.connect(app.quit)
layout.addWidget(exit_button)

# Set the layout on the main window
main_window.setLayout(layout)

clicked = Signal(Qt.MouseButton)

# Show the main window
main_window.show()

sys.exit(app.exec())