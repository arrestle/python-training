import sys, os
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import QUrl
from PySide6.QtQuick import QQuickView

if __name__ == "__main__":
    app = QGuiApplication()
    view = QQuickView()

    # set the import_path to be the modules subfolder
    import_path = os.path.join(os.path.dirname(__file__), "modules")

    view.engine().addImportPath(import_path)
    view.setSource(QUrl.fromLocalFile(os.path.join(import_path, "example7.qml")))

    #view.loadFromModule("Main", "Main")
    view.setResizeMode(QQuickView.SizeRootObjectToView)
    view.show()

    # # add a second view to show the module example7
    # view2 = QQuickView()
    # view2.engine().addImportPath(import_path)

    # # set the source to the module example7 from the qmldir file
    # view2.loadFromModule("example7", "example7")
    # view2.setResizeMode(QQuickView.SizeRootObjectToView)
    # view2.show()

    #     # Check for errors
    # if view2.status() == QQuickView.Error:
    #     for error in view2.errors():
    #         print(error.toString())

    ex = app.exec()
    del view
    # del view2
    sys.exit(ex)
