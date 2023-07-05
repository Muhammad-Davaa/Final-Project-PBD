from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def halaman_home():
    css_url = url_for('static', filename='css/style.css');
    return render_template("home.html", css_url=css_url);

@app.route("/login")
def halaman_login():
    return render_template("login.html");

@app.route("/registrasi")
def halaman_registrasi():
    return render_template("registrasi.html");

@app.route("/member")
def data_member():
    return render_template("member.html");

@app.route("/transaksi_member")
def data_transaksi_memer():
    return render_template("transaksi_member.html");

@app.route("/transaksi_umum")
def data_transaksi_umum():
    return render_template("transaksi_umum.html");

@app.route("/cetak_laporan")
def cetak_laporan():
    return render_template("cetak_laporan.html");

@app.route("/contac")
def hub_contact():
    return render_template("contact.html");


if __name__ == "__main__":
    app.run(debug=True)