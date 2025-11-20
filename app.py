from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Carregar códigos OBD2
with open("codes.json", "r", encoding="utf-8") as f:
    codes = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/buscar", methods=["POST"])
def buscar():
    code = request.form.get("code", "").strip().upper()

    if not code:
        return render_template("notfound.html",
                               message="Você precisa digitar um código OBD2.",
                               searched_code=code)

    data = codes.get(code)
    if data:
        return render_template("result.html",
                               code=code,
                               description=data.get("description"),
                               causes=data.get("causes", []),
                               video=data.get("video"))
    else:
        return render_template("notfound.html",
                               message=f"O código {code} não foi encontrado.",
                               searched_code=code)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
