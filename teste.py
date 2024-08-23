from src.database.database import create_connection, close_connection

# Criar conexão
connection = create_connection()

if connection:
    try:
        # Executar uma consulta
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM sua_tabela")

        # Exibir resultados
        result = cursor.fetchall()
        for row in result:
            print(row)

    finally:
        # Fechar conexão
        cursor.close()
        close_connection(connection)