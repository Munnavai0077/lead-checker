from flask import Flask, request

app = Flask(__name__)

HTML_FORM = """
<!doctype html>
<html>
<head>
    <title>Lead Checker</title>
</head>
<body>
    <h1>Lead Classification</h1>
    <form method="post">
        <label>Role:</label>
        <input type="text" name="role"><br><br>
        <label>Industry/Company Info:</label>
        <input type="text" name="industry"><br><br>
        <input type="submit" value="Check">
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        role = request.form.get("role", "")
        industry = request.form.get("industry", "")
        result = f"Role: {role} | Industry: {industry}"
        return HTML_FORM + "<p>" + result + "</p>"
    return HTML_FORM

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
