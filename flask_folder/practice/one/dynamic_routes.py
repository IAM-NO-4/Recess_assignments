from flask import Flask
app = Flask(__name__)

@app.route("/details/<name>")
def student(name):
    return f"{name } is a good student"

@app.route("/get/<name>/<int:score>")
def scoredetails(name, score):
    return f"{name} got {score} marks"

if __name__ == "__main__":
    app.run(debug=True)