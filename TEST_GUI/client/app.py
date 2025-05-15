from flask import Flask, render_template, request, redirect
import pandas as pd
import tenseal as ts
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

df_global = None  # pour stocker temporairement les données

@app.route("/", methods=["GET", "POST"])
def index():
    global df_global

    if request.method == "POST":
        file = request.files["file"]
        if file.filename.endswith(".xlsx"):
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            df = pd.read_excel(filepath, usecols=[0, 1, 2])
            df.columns = ['id', 'HR_min', 'HR_max']
            df_global = df  # sauvegarde temporaire

            return render_template("index.html", data=df.to_html(index=False))

    return render_template("index.html", data=None)

@app.route("/encrypt")
def encrypt():
    global df_global
    if df_global is None:
        return redirect("/")

    # Chiffrement
    context = ts.context(ts.SCHEME_TYPE.BFV, poly_modulus_degree=8192, plain_modulus=1032193)
    context.global_scale = 2**40
    context.generate_galois_keys()

    enc_id = ts.bfv_vector(context, df_global["id"].tolist())
    enc_min = ts.bfv_vector(context, df_global["HR_min"].tolist())
    enc_max = ts.bfv_vector(context, df_global["HR_max"].tolist())



if __name__ == "__main__":
    app.run(debug=True)
