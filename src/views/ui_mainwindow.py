from PyQt6.QtWidgets import QMainWindow, QMenuBar, QVBoxLayout, QWidget, QTableWidget
from src.controllers.controllers import Controller

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema de Inventário")
        self.setGeometry(300, 200, 800, 600)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout(self.main_widget)

        # Menu
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)
        self.menu = self.menu_bar.addMenu("Menu")

        # Controlador
        self.controller = Controller(self)

        # Tabela dinâmica
        self.table_widget = QTableWidget()
        self.layout.addWidget(self.table_widget)

        self.controller.setup_menu()
