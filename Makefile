
mainwindow_ui.py: mainwindow.ui
	pyside6-uic mainwindow.ui -o mainwindow_ui.py

# Optional: Define a default target
all: mainwindow_ui.py

clean:
	rm -f mainwindow_ui.py
