from flask import Flask, request

app = Flask(__name__)

HTML_FORM = """
<!doctype html>
<html>
<head>
    <title>Lead Checker</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: Arial, sans-serif;
            background: #f2f4f7;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            text-align: center;
            width: 400px;
        }
        h2 {
            margin-bottom: 20px;
            color: #333;
        }
        input[type=text] {
            padding: 10px;
            margin: 10px 0;
            width: 90%;
            border: 1px solid #ccc;
            border-radius: 8px;
        }
        button {
            padding: 10px 20px;
            background: #4CAF50;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }
        button:hover {
            background: #45a049;
        }
        .result {
            margin-top: 20px;
            font-size: 14px;
            color: #333;
            text-align: left;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Lead Classification</h2>
        <form method="POST">
            <input type="text" name="role" placeholder="Role"><br>
            <input type="text" name="industry" placeholder="Industry/Company Info"><br>
            <button type="submit">Check</button>
        </form>
        {result}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        role = request.form.get("role", "").strip()
        industry = request.form.get("industry", "").strip()

        # check role only if user entered something
        role_result = ""
        if role:
            if "chief operating officer" in role.lower():
                role_result = f"Role: {role} → ✅ It is correct<br>"
            else:
                role_result = f"Role: {role} → ❌ It is wrong<br>"

        # industry check
        industry_result = ""
        final = ""
        if industry:
            if any(word in industry.lower() for word in ["saas", "ai", "cloud", "automation", "software"]):
                industry_result = f"Industry: {industry} → Falls under the 6 targeted industries<br>"
                final = "Final: ✅ Green (Good Industry)"
            else:
                industry_result = f"Industry: {industry} → Does not fall under the 6 targeted industries<br>"
                final = "Final: ❌ Red (Not a Match)"

        result = f"<div class='result'>{role_result}{industry_result}{final}</div>"

    return HTML_FORM.format(result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
