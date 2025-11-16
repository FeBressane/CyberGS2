
import sqlite3

def buscar_usuario_seguro(email: str):
    """Exemplo corrigido usando parâmetros na query."""
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    # CORRETO: uso de parâmetros evita SQL Injection
    query = "SELECT id, nome, email FROM usuarios WHERE email = ?"
    cursor.execute(query, (email,))

    resultados = cursor.fetchall()
    conn.close()
    return resultados


def main():
    email = input("Digite o seu email: ")
    usuarios = buscar_usuario_seguro(email)
    print("Resultado da busca:", usuarios)


if __name__ == "__main__":
    main()
