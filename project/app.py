from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from functions import wrong, is_strong_password, login_required
app = Flask(__name__)

db = SQL("sqlite:///project.db")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response



@app.route("/", methods=["GET", "POST"])
@login_required
def index():
        return render_template("index.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form.get("password") is not None and request.form.get("password") is not None:
            check = db.execute("SELECT * FROM users WHERE nickname = (?)", request.form.get("username") )
            if len(check) != 1 or not check_password_hash(check[0]["hashed_p"], request.form.get("password")):
                return wrong("wrong password or username", 400)
            else:
                session["user_id"] = check[0]["id"]
                return redirect("/")
        else:
            return wrong("Please give password and username", 400)
    else:
        return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if not request.form.get("pass") and not request.form.get("user") and not request.form.get("user") and not request.form.get("mail"):
            if not request.form.get("confirmation"):
                return wrong("to register u need to confirm password", 400)
            else:
                return wrong("to register u need to give username,password and email adress", 400)

        else:
            rows = db.execute("SELECT * FROM users WHERE nickname = ?", request.form.get("user"))
            rows2 = db.execute("SELECT * FROM users WHERE email = ?", request.form.get("mail"))
            if len(rows) > 0:
                return wrong("Username already exists", 400)
            else:
                if len(rows2) > 0:
                    return wrong("There is already account made with this email", 400)
                else:
                    if is_strong_password(request.form.get("pass")):
                        if request.form.get("pass") == request.form.get("confirmation"):
                            db.execute("INSERT INTO users (nickname, hashed_p, email) VALUES (?,?,?) ", request.form.get("user"),generate_password_hash(request.form.get("pass")), request.form.get("mail"))
                            return render_template("login.html")
                        else:
                            return wrong("Passwords didn't match", 400)
                    else:
                        return wrong("Weak password", 400)

    else:
        return render_template("register.html")


@app.route("/history", methods=["GET", "POST"])
@login_required
def history():
    historys = db.execute("SELECT * FROM history JOIN types ON history.kapi_typeH = types.id WHERE history.id = ?", session["user_id"])
    print(historys)
    if request.method == "POST":
        return render_template("history.html")
    else:
        return render_template("history.html", historys=historys)


@app.route("/quiz", methods=["GET", "POST"])
@login_required
def quiz():
    if request.method == "POST":

        return render_template("quiz.html")
    else:
        return render_template("quiz.html")


@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.clear()
    return redirect("/")

@app.route("/answer", methods=["GET", "POST"])
@login_required
def answer():
    capurl = db.execute("SELECT * FROM types WHERE id=(?)", request.args.get('type'))
    if request.method == "POST":
        capybara_type = request.form.get('type')
        print(capybara_type)
        return "Success"
    else:
        capybara_type = request.args.get('type')
        db.execute("INSERT INTO history(id, kapi_typeH) VALUES(?, ?)", session["user_id"], request.args.get('type'))
        return render_template("answer.html",capurls=capurl, capybara_type=capybara_type)

if __name__ == "__main__":
    app.run(debug=True)
