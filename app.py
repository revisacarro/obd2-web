from flask import Flask, render_template, request, redirect, url_for, flash
import json

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Carregar a base de códigos OBD2
with open("codes.json", "r") as f:
    codes = json.load(f)

# Página inicial
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        code = request.form.get("code").upper()
        return redirect(url_for("result", code=code))
    return render_template("index.html")

# Página de resultado / explicação
@app.route("/result/<code>")
def result(code):
    info = codes.get(code)
    return render_template("result.html", code=code, info=info)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
