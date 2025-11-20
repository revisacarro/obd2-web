from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Carregar base de códigos OBD2
with open("codes.json", "r", encoding="utf-8") as f:
    codes = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/buscar", methods=["POST"])
def buscar():
    code = request.form.get("code", "").strip().upper()

    # Se o usuário enviar algo vazio
    if not code:
        return render_template("notfound.html",
                               message="Você precisa digitar um código OBD2.",
                               searched_code=code)

    # Procurar o código no JSON
    data = codes.get(code)

    # Se encontrou → enviar para o result.html
    if data:
        return render_template("result.html",
                               code=code,
                               description=data.get("description"),
                               causes=data.get("causes", []),
                               video=data.get("video"))
    
    # Se não encontrou → enviar para o notfound.html
    return render_template("notfound.html",
                           message=f"O código {code} não foi encontrado.",
                           searched_code=code)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
