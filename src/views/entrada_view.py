from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton
from src.database.database import Database

class EntradaView:
    def __init__(self, main_window):
        self.main_window = main_window
        self.db = Database()

    def display(self):
        if hasattr(self.main_window, 'input_frame'):
            self.main_window.input_frame.show()
            self.clear_frame()

            nome_label = QLabel("Nome do Material:")
            self.nome_input = QLineEdit()

            quantidade_label = QLabel("Quantidade:")
            self.quantidade_input = QLineEdit()

            confirmar_button = QPushButton("Confirmar Entrada")
            confirmar_button.clicked.connect(self.confirmar_entrada)

            self.main_window.input_layout.addWidget(nome_label)
            self.main_window.input_layout.addWidget(self.nome_input)
            self.main_window.input_layout.addWidget(quantidade_label)
            self.main_window.input_layout.addWidget(self.quantidade_input)
            self.main_window.input_layout.addWidget(confirmar_button)
        else:
            print("O atributo 'input_frame' não foi definido no main_window.")


    def confirmar_entrada(self):
        nome = self.nome_input.text()
        quantidade = int(self.quantidade_input.text())
        self.db.insert_entrada(nome, quantidade)
        self.main_window.controller.estoque_view.display()

    def clear_frame(self):
        while self.main_window.input_layout.count():
            child = self.main_window.input_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
