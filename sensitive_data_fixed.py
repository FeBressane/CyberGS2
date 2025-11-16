
import hashlib
import os
from typing import Tuple, Dict, Any

usuarios_seguro: Dict[str, Dict[str, Any]] = {}


def gerar_hash_senha(senha: str, salt: bytes | None = None) -> Tuple[bytes, bytes]:
    """Gera hash seguro para a senha usando PBKDF2-HMAC-SHA256."""
    if salt is None:
        salt = os.urandom(16)
    senha_hash = hashlib.pbkdf2_hmac(
        "sha256",
        senha.encode("utf-8"),
        salt,
        100_000,
    )
    return salt, senha_hash


def cadastrar_usuario_seguro(username: str, senha: str):
    salt, senha_hash = gerar_hash_senha(senha)
    usuarios_seguro[username] = {
        "username": username,
        "salt": salt.hex(),
        "senha_hash": senha_hash.hex(),
    }
    # CORRETO: não exibir a senha em logs
    print(f"Usuário {username} cadastrado com segurança.")


def main():
    nome = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    cadastrar_usuario_seguro(nome, senha)
    print("Usuário cadastrado de forma segura.")


if __name__ == "__main__":
    main()
