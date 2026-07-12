from flask import Flask, render_template
app = Flask(__name__)

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/index/<name>/<age>")
def home(name, age):
    return render_template("home.html", username = name, your_age = age )

if __name__ == "__main__":
    app.run(debug=True)

