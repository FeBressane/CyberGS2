
from flask import Flask, request

app = Flask(__name__)

@app.route("/comentarios")
def comentarios():
    comentario = request.args.get("comentario", "")
    # VULNERÁVEL: o conteúdo do usuário é inserido diretamente no HTML
    html = f"""<html>
    <head><title>Comentários</title></head>
    <body>
        <h1>Comentários</h1>
        <p>{comentario}</p>
    </body>
    </html>"""
    return html


if __name__ == "__main__":
    # NÃO usar debug=True em produção; aqui é apenas exemplo didático
    app.run(host="0.0.0.0", port=5000, debug=True)
