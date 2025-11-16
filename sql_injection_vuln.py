
import sqlite3

def buscar_usuario(email: str):
    """Exemplo intencionalmente vulnerável a SQL Injection."""
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    # VULNERÁVEL: concatenação direta do input do usuário na query
    query = f"SELECT id, nome, email FROM usuarios WHERE email = '{email}'"
    print("[DEBUG] Executando query:", query)
    cursor.execute(query)

    resultados = cursor.fetchall()
    conn.close()
    return resultados


def main():
    email = input("Digite o seu email: ")
    usuarios = buscar_usuario(email)
    print("Resultado da busca:", usuarios)


if __name__ == "__main__":
    main()
