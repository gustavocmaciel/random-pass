from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("new-password")
def new_password:

    # Generate new password
    if request.method == "POST":
        length = request.form.get("name")
        new_password = generate_password(length)
        return render_template("new_password.html", new_password=new_password)
