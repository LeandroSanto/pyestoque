import sqlite3

class Database:
    def __init__(self, db_name="inventory.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Criação das tabelas de estoque e histórico
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS estoque (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL,
                                quantidade INTEGER NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS historico (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL,
                                quantidade INTEGER NOT NULL,
                                tipo TEXT NOT NULL,
                                solicitante TEXT,
                                data DATE DEFAULT CURRENT_TIMESTAMP)''')

        self.conn.commit()

    def get_estoque(self):
        self.cursor.execute("SELECT nome, quantidade FROM estoque")
        return self.cursor.fetchall()

    def get_historico(self):
        self.cursor.execute("SELECT nome, quantidade, tipo, solicitante, data FROM historico")
        return self.cursor.fetchall()

    def insert_entrada(self, nome, quantidade):
        self.cursor.execute("INSERT INTO estoque (nome, quantidade) VALUES (?, ?) ON CONFLICT(nome) DO UPDATE SET quantidade = quantidade + ? WHERE nome = ?", (nome, quantidade, quantidade, nome))
        self.cursor.execute("INSERT INTO historico (nome, quantidade, tipo) VALUES (?, ?, 'Entrada')", (nome, quantidade))
        self.conn.commit()

    def insert_saida(self, nome, quantidade, solicitante):
        self.cursor.execute("UPDATE estoque SET quantidade = quantidade - ? WHERE nome = ?", (quantidade, nome))
        self.cursor.execute("INSERT INTO historico (nome, quantidade, tipo, solicitante) VALUES (?, ?, 'Saída', ?)", (nome, quantidade, solicitante))
        self.conn.commit()
