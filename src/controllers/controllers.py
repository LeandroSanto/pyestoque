from PyQt6.QtGui import QAction
from src.views.estoque_view import EstoqueView
from src.views.entrada_view import EntradaView
from src.views.saida_view import SaidaView

class Controller:
    def __init__(self, main_window):
        self.main_window = main_window

        # Views
        self.estoque_view = EstoqueView(main_window)
        self.entrada_view = EntradaView(main_window)
        self.saida_view = SaidaView(main_window)

    def setup_menu(self):
        # Configurações do menu e ações
        exibir_estoque_action = QAction("Exibir Estoque", self.main_window)
        exibir_estoque_action.triggered.connect(self.estoque_view.display)

        entrada_item_action = QAction("Entrada de Item", self.main_window)
        entrada_item_action.triggered.connect(self.entrada_view.display)

        saida_item_action = QAction("Saída de Item", self.main_window)
        saida_item_action.triggered.connect(self.saida_view.display)

        historico_saida_action = QAction("Histórico de Saída", self.main_window)
        historico_saida_action.triggered.connect(self.estoque_view.display_historico)

        # Adicionando ao menu
        menu = self.main_window.menu
        menu.addAction(exibir_estoque_action)
        menu.addAction(entrada_item_action)
        menu.addAction(saida_item_action)
        menu.addAction(historico_saida_action)
