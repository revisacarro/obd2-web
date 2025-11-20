from flask import Flask, render_template, request
import json
from datetime import datetime

app = Flask(__name__)

# carregar códigos
with open("codes.json", "r") as f:
    codes = json.load(f)

# Injetar ano no template para rodapé
@app.context_processor
def inject_year():
    return {"current_year": datetime.now().year}

@app.route("/")
def home():
    return render_template("index.html", title="OBD2 Web")

@app.route("/result", methods=["POST"])
def result():
    code = request.form.get("code", "").strip().upper()
    data = codes.get(code)
    return render_template("result.html", data=data, title=f"Resultado {code}")

@app.route("/diagnostico-guiado")
def diagnostico_guiado():
    return render_template("diagnostico_guiado.html", title="Diagnóstico Guiado")

@app.route("/about")
def about():
    return "<h2>Sobre</h2><p>Página ainda em desenvolvimento.</p>"

@app.route("/popular")
def popular():
    return "<h2>Códigos Populares</h2><p>Em breve.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
