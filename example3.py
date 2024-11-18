import sys
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog, QTableWidget, QTableWidgetItem, QLabel, QHBoxLayout, QTreeWidget, QTreeWidgetItem)

from PySide6.QtGui import QColor
from PySide6.QtCore import Qt

def get_rgb_from_hex(code):
    code_hex = code.replace("#", "")
    rgb = tuple(int(code_hex[i:i+2], 16) for i in (0, 2, 4))
    return QColor.fromRgb(rgb[0], rgb[1], rgb[2])

class Form(QDialog):
    def get_rgb_from_hex(code):
        code_hex = code.replace("#", "")
        rgb = tuple(int(code_hex[i:i+2], 16) for i in (0, 2, 4))
        return QColor.fromRgb(rgb[0], rgb[1], rgb[2])
    
    colors = [("Red", "#FF0000"),
          ("Green", "#00FF00"),
          ("Blue", "#0000FF"),
          ("Black", "#000000"),
          ("White", "#FFFFFF"),
          ("Electric Green", "#41CD52"),
          ("Dark Blue", "#222840"),
          ("Yellow", "#F9E56d")]
    
    treedata = {"Project A": ["file_a.py", "file_a.txt", "something.xls"],
        "Project B": ["file_b.csv", "photo.jpg"],
        "Project C": []}

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        self.edit = QLineEdit("Write my name here")
        self.button = QPushButton("Show Greetings")
        self.exit_button = QPushButton("Exit")

        # make the exitbutton light red
        self.exit_button.setStyleSheet("background-color: lightcoral")
        self.button.setStyleSheet("background-color: lightgreen")

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        # Create a horizontal layout for the buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button)
        button_layout.addWidget(self.exit_button)

        # Add the button layout to the main layout
        layout.addLayout(button_layout)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button.clicked.connect(self.greetings)
        self.exit_button.clicked.connect(app.quit)

        table = QTableWidget()
        table.setRowCount(len(self.colors))
        table.setColumnCount(len(self.colors[0]) + 1)
        table.setHorizontalHeaderLabels(["Name", "Hex Code", "Color"])

        for i, (name, code) in enumerate(self.colors):
            item_name = QTableWidgetItem(name)
            item_code = QTableWidgetItem(code)
            item_color = QTableWidgetItem()
            item_color.setBackground(get_rgb_from_hex(code))
            table.setItem(i, 0, item_name)
            table.setItem(i, 1, item_code)
            table.setItem(i, 2, item_color)
        layout.addWidget(table)
        self.setLayout(layout)

        tree = QTreeWidget()
        tree.setColumnCount(3)
        tree.setHeaderLabels(["Name", "Type","Size"])
        items = []
        for key, values in self.treedata.items():
            item = QTreeWidgetItem([key])
            for value in values:
                ext = value.split(".")[-1].lower()
                child = QTreeWidgetItem([value, ext, "100KB"])
                item.addChild(child)
            items.append(item)

        tree.insertTopLevelItems(0, items)
        layout.addWidget(tree)

        w = QLabel("This is centered text")
        w.setAlignment(Qt.AlignCenter)
        layout.addWidget(w)


             # Set size policy for the main window
        #self.setSizePolicy(QWidget.Expanding, QWidget.Expanding)
        self.setMinimumSize(500, 600)
        


    # Greets the user
    def greetings(self):
        print(f"Hello {self.edit.text()}")

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())