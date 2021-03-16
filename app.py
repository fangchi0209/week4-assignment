from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
app=Flask(__name__, static_folder="static", static_url_path="/static")
app.secret_key ="abc"

@app.route("/")
def index():
    return render_template("loginpage.html")


@app.route("/signin", methods=["POST"])
def signin():

    if request.form["username"]=="test" and request.form["password"]=="test":
        session["username"]=request.form["username"]
        return redirect("http://127.0.0.1:3000/member")

    else:
        return redirect("http://127.0.0.1:3000/error")


@app.route("/member")
def member():
    # return render_template("member.html")
    if "username" in session:
        return render_template("member.html")
    else:
        return redirect("http://127.0.0.1:3000/")


@app.route("/error")
def error():
    return render_template("error.html")

@app.route("/signout")
def signout():
    session.pop("username", None)
    return redirect("http://127.0.0.1:3000/")



app.run(port=3000)