from src.database.database import Database

class EstoqueView:
    def __init__(self, main_window):
        self.main_window = main_window
        self.db = Database()

    def display(self):
        self.main_window.input_frame.hide()
        rows = self.db.get_estoque()

        self.main_window.table_widget.setRowCount(len(rows))
        self.main_window.table_widget.setColumnCount(2)
        self.main_window.table_widget.setHorizontalHeaderLabels(["Nome", "Quantidade"])

        for i, row in enumerate(rows):
            self.main_window.table_widget.setItem(i, 0, QTableWidgetItem(row[0]))
            self.main_window.table_widget.setItem(i, 1, QTableWidgetItem(str(row[1])))

    def display_historico(self):
        self.main_window.input_frame.hide()
        rows = self.db.get_historico()

        self.main_window.table_widget.setRowCount(len(rows))
        self.main_window.table_widget.setColumnCount(5)
        self.main_window.table_widget.setHorizontalHeaderLabels(["Nome", "Quantidade", "Tipo", "Solicitante", "Data"])

        for i, row in enumerate(rows):
            for j, val in enumerate(row):
                self.main_window.table_widget.setItem(i, j, QTableWidgetItem(str(val)))
