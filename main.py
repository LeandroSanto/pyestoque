from PyQt6.QtWidgets import QApplication
from src.views.ui_mainwindow import MainWindow
from src.views.entrada_view import EntradaView

if __name__ == "__main__":
    app = QApplication([])

    main_window = MainWindow()
    entrada_view = EntradaView(main_window)

    main_window.show()
    app.exec()
