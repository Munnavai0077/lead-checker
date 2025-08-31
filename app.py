from flask import Flask, request

app = Flask(__name__)

HTML_FORM = """
<!doctype html>
<html>
<head>
    <title>Lead Checker</title>
</head>
<body>
    <h2>Lead Classification</h2>
    <form method="post">
        Role: <input type="text" name="role"><br><br>
        Industry/Company Info: <input type="text" name="industry"><br><br>
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

        return f"""
        <h3>Result</h3>
        Role: {role}<br>
        Industry: {industry}<br>
        Final: ✅ Green (Good Lead) [demo]
        """
    return HTML_FORM


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
