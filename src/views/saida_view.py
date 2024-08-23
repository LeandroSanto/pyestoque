from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QComboBox
from src.database.database import Database

class SaidaView:
    def __init__(self, main_window):
        self.main_window = main_window
        self.db = Database()

    def display(self):
        self.main_window.input_frame.show()
        self.clear_frame()

        nome_label = QLabel("Nome do Material:")
        self.nome_combo = QComboBox()

        rows = self.db.get_estoque()
        for row in rows:
            self.nome_combo.addItem(row[0])

        quantidade_label = QLabel("Quantidade:")
        self.quantidade_input = QLineEdit()

        solicitante_label = QLabel("Solicitante:")
        self.solicitante_input = QLineEdit()

        confirmar_button = QPushButton("Confirmar Saída")
        confirmar_button.clicked.connect(self.confirmar_saida)

        self.main_window.input_layout.addWidget(nome_label)
        self.main_window.input_layout.addWidget(self.nome_combo)
        self.main_window.input_layout.addWidget(quantidade_label)
        self.main_window.input_layout.addWidget(self.quantidade_input)
        self.main_window.input_layout.addWidget(solicitante_label)
        self.main_window.input_layout.addWidget(self.solicitante_input)
        self.main_window.input_layout.addWidget(confirmar_button)

    def confirmar_saida(self):
        nome = self.nome_combo.currentText()
        quantidade = int(self.quantidade_input.text())
        solicitante = self.solicitante_input.text()
        self.db.insert_saida(nome, quantidade, solicitante)
        self.main_window.controller.estoque_view.display()

    def clear_frame(self):
        while self.main_window.input_layout.count():
            child = self.main_window.input_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
