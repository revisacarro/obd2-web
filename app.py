from flask import Flask, render_template, request
import json
import os
from datetime import datetime

app = Flask(__name__)

# Caminho absoluto do JSON
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(BASE_DIR, "codes.json")

# Carrega códigos do JSON
with open(json_path, "r", encoding="utf-8") as f:
    codes = json.load(f)

# Injeta ano atual no template
@app.context_processor
def inject_year():
    return {"current_year": datetime.now().year}

# Página inicial
@app.route("/")
def home():
    return render_template("index.html", title="OBD2 Web")

# Página de resultados
@app.route('/result', methods=['POST'])
def result():
    code = request.form.get('codigo', '').strip().upper()
    info = next((c for c in codes if c["codigo"].upper() == code), None)
    return render_template('result.html', info=info)

# Outras páginas (opcional)
@app.route("/diagnostico-guiado")
def diagnostico_guiado():
    return render_template("diagnostico_guiado.html", title="Diagnóstico Guiado")

@app.route("/produtos")
def produtos():
    return render_template("produtos.html", title="Produtos Recomendados")

@app.route("/about")
def about():
    return render_template("about.html", title="Sobre o Projeto")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
