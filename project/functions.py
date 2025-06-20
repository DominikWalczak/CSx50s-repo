from flask import redirect, render_template, session
import re
from flask import redirect, render_template, session
from functools import wraps


def login_required(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def wrong(message, code=400):
    def escape(s):
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("wrong.html", top=code, bottom=escape(message)), code

def is_strong_password(password):
    if len(password) < 8:
        return False

    if not any(c.isupper() for c in password):
        return False

    if not any(c.islower() for c in password):
        return False

    if not any(c.isdigit() for c in password):
        return False

    if not re.search(r"[!@#\$%\^&\*\(\)_\+\{\[\]:;<>,\.\?~\\|/-]", password):
        return False

    return True
