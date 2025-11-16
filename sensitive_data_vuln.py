
# Exemplo de exposição de dados sensíveis: senha em texto puro e log de informações sensíveis.

usuarios = {}


def cadastrar_usuario(username: str, senha: str):
    # VULNERÁVEL: salvando senha em texto puro
    usuarios[username] = {
        "username": username,
        "senha": senha,
    }
    # VULNERÁVEL: logando senha no console
    print(f"[DEBUG] Novo usuário: {username}, senha={senha}")


def main():
    nome = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    cadastrar_usuario(nome, senha)
    print("Usuário cadastrado (de forma insegura).")


if __name__ == "__main__":
    main()
