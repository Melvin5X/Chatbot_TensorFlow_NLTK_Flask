from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def home():
    return "welcome"

@app.route("/hi/<name>")
def hello(name):
    return "Hi {}".format(name)

@app.route("/greet/<name>")
def greet(name):
    return redirect(url_for("hello", name=name))

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method =="GET":
        username = request.args.get("username")
        return redirect(url_for("hello", name = username))
    else:
        username = request.form["username"]
        return redirect(url_for('hello', name = username))


if __name__ =="__main__":
    app.run(port = 4002, debug = True)