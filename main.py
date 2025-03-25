import flask


# your academic email
AUTHOR = "aluk@seas.upenn.edu"


app = flask.Flask(__name__)

# This endpoint returns a simple greeting message.
@app.route("/")
def hello():
    return f"Hello from my Password Validator! &mdash; <tt>{AUTHOR}</tt>", 200

# This endpoint validates the provided password according to the following policy:
#   - Length >= 8
#   - Contains at least 1 uppercase letter
#   - Contains at least 1 digit
#   - Contains at least 1 special character: !@#$%^&*
@app.route("/v1/checkPassword", methods=["POST"])
def check_password():
    data = flask.request.get_json() or {}
    password = data.get("password", "")
    reasons = []

    if len(password) < 8:
        reasons.append("Password must be at least 8 characters long.")
    if not any(c.isupper() for c in password):
        reasons.append("Password must contain at least one uppercase letter.")
    if not any(c.isdigit() for c in password):
        reasons.append("Password must contain at least one digit.")
    if not any(c in "!@#$%^&*" for c in password):
        reasons.append("Password must contain at least one special character (!@#$%^&*).")

    valid = len(reasons) == 0
    reason_str = "" if valid else " ".join(reasons)

    return flask.jsonify({"valid": valid, "reason": reason_str}), 200

if __name__ == "__main__":
    app.run(debug=True)
