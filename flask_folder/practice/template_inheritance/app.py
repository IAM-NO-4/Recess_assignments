from flask import Flask, render_template,flash,request,redirect,url_for
import random
app = Flask(__name__)
x = random.randint(1,192666666666666)
app.secret_key = str(x)

@app.route("/index")
def student():
    return render_template("index.html")

@app.route("/login",methods= ["POST","get"])
def register():
    if request.method == "POST":
        flash("login successful","sucess")
        return redirect(url_for('student'))
    return render_template("form.html")



if __name__ == "__main__":
    app.run(debug=True)