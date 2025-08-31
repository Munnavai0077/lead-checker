from flask import Flask, render_template_string, request

app = Flask(__name__)

# Example target roles (you can expand later with full list)
TARGET_ROLES = ["Chief Operating Officer", "Director of Quality Assurance", "Vice President Software Engineering"]

# Example target industries
TARGET_INDUSTRIES = [
    "SaaS", "Technology & IT Services", "Cloud Solutions & Enterprise Software",
    "AI / Machine Learning / Automation", "Digital Transformation & Consulting Firms",
    "B2B Software / Enterprise Applications"
]

HTML_FORM = """
<!doctype html>
<title>Lead Checker</title>
<h2>Lead Classification</h2>
<form method=post>
  Role: <input type=text name=role><br><br>
  Industry/Company Info: <input type=text name=industry><br><br>
  <input type=submit value=Check>
</form>
<p><pre>{{ result }}</pre></p>
"""

@app.route("/", methods=["GET", "POST"])
def classify():
    result = ""
    if request.method == "POST":
        role = request.form["role"].strip()
        industry = request.form["industry"].strip()

        if role:  # Role + Industry
            role_check = "It is correct" if role in TARGET_ROLES else "It is wrong"
            industry_check = "Falls under the 6 targeted industries" if any(t in industry for t in TARGET_INDUSTRIES) else "Does not fall under the 6 targeted industries"
            final = "✅ Green (Good Lead)" if role_check == "It is correct" and "Falls under" in industry_check else "❌ Red (Not a Match)"
            result = f"Role: {role} → {role_check}\nIndustry: {industry} → {industry_check}\nFinal: {final}"
        else:  # Only Industry
            industry_check = "Falls under the 6 targeted industries" if any(t in industry for t in TARGET_INDUSTRIES) else "Does not fall under the 6 targeted industries"
            final = "✅ Green (Good Industry)" if "Falls under" in industry_check else "❌ Red (Not a Match)"
            result = f"Industry: {industry} → {industry_check}\nFinal: {final}"

    return render_template_string(HTML_FORM, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
