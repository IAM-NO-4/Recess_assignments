from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/login",methods= ["POST","get"])
def register():
    if request.method == "POST":
        name = request.form.get("name","Guest")
        contact = request.form.get("contact")
        email = request.form["email"]
        password = request.form.get("password")
        return f"Hello {name}, your email is {email} and your contact is {password}"
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)