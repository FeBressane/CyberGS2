
from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/comentarios")
def comentarios_seguro():
    comentario = request.args.get("comentario", "")
    # CORRETO: escapar o conteúdo antes de exibir
    comentario_seguro = escape(comentario)
    html = f"""<html>
    <head><title>Comentários</title></head>
    <body>
        <h1>Comentários</h1>
        <p>{comentario_seguro}</p>
    </body>
    </html>"""
    return html


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
