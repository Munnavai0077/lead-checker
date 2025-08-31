from flask import Flask, request

app = Flask(__name__)

# 🎯 Target roles and industries
TARGET_ROLES = [
    "Vice President of Software Engineering",
    "Senior Software Engineering Manager",
    "Director of Quality Assurance",
    "Human Resources Director",
    "Senior Information Technology Manager",
    "Senior Recruitment Manager",
    "Chief Product Officer",
    "Senior Director Quality Assurance",
    "Associate Director Quality Assurance",
    "Director Software Quality Assurance",
    "Director of Analytics",
    "Chief Technology Officer",
    "Chief Innovation Officer",
    "Director of Software Engineering",
    "Director of Information Technology",
    "Chief People Officer",
    "Software Engineering Manager",
    "Head of Talent Management",
    "Engineering Manager",
    "Vice President Talent Acquisition",
    "Senior Manager Talent Acquisition",
    "Head of Web Development",
    "Head of Engineering",
    "Senior Manager Quality Engineering",
    "Vice President of Product Management",
    "Chief Information Officer",
    "Senior SAP Project Manager",
    "Senior Human Resources Partner",
    "Senior Director of Software Engineering",
    "SAP Project Manager",
    "Information Technology Operations Project Manager",
    "Cloud Architect",
    "Director Data Science",
    "Head of Data Science",
    "Chief Digital Officer",
    "Head of Machine Learning",
    "Manager of Artificial Intelligence",
    "Director of Artificial Intelligence",
    "Vice President of Artificial Intelligence",
    "Information Technology Service Management Specialist",
    "Vice President of Digital Transformation",
    "Product Manager",
    "Senior Product Manager",
    "Director Application Development",
    "Chief Operating Officer",
    "Head of Product",
    "Director Information Technology Operations",
    "DevOps Manager",
    "Director of DevOps",
    "Head of DevOps",
    "Chief Information Technology Officer",
    "Quality Assurance Team Lead",
    "Director of Engineering",
    "Head of Procurement",
    "Head of Product Management",
    "Director of Technology",
    "Senior Quality Assurance Manager",
    "Senior Human Resources Business Partner",
    "Head of Recruitment",
    "Technology Manager",
    "Vice President Quality Assurance",
    "Head of Information Technology Department",
    "Senior Procurement Manager",
    "Vice President of Engineering",
    "Director SAP",
    "Head of Quality Assurance",
    "Senior Technical Project Manager",
    "Senior Vice President of Technology",
    "Senior Director of Product Management",
    "Head of Software",
    "Technical Project Manager",
    "Procurement Manager",
    "Delivery Manager",
    "Human Resources Business Partner",
    "Human Resources Business Manager",
    "Information Technology Manager",
    "Director of Product Management",
    "Senior Vice President Information Technology",
    "Talent Director",
    "Head of Information Technology",
    "Director Information Technology Infrastructure",
    "Recruiting Manager",
    "Vice President Information Technology",
    "Head of Software Engineering",
    "Vice President of Technology",
    "Head of Human Resources",
    "Transformation Director",
    "Senior Vice President of Engineering",
    "Director Talent Acquisition",
    "Chief Executive Officer",
    "Director of Operations",
    "Head of Information Technology Operations",
    "Director of Product Development",
    "Information Technology Service Delivery Manager",
    "Director Enterprise Resources Planning",
    "Enterprise Architect",
    "Director Quality Engineering",
    "Software Test Manager",
    "Quality Assurance Test Manager",
    "Director of Recruiting"
]

TARGET_INDUSTRIES = [
    "SaaS (Software as a Service)",
    "Technology & IT Services",
    "Cloud Solutions & Enterprise Software",
    "AI / Machine Learning / Automation",
    "Digital Transformation & Consulting Firms",
    "B2B Software / Enterprise Applications"
]

# 🎨 HTML Form with styling
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
            border-radius: 6px;
        }
        button {
            padding: 10px 20px;
            border: none;
            border-radius: 6px;
            background: #007bff;
            color: white;
            cursor: pointer;
        }
        button:hover {
            background: #0056b3;
        }
        .result {
            margin-top: 20px;
            padding: 15px;
            border-radius: 8px;
            font-weight: bold;
        }
        .green { background: #d4edda; color: #155724; }
        .yellow { background: #fff3cd; color: #856404; }
        .red { background: #f8d7da; color: #721c24; }
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
    result_html = ""
    if request.method == "POST":
        role = request.form.get("role", "").strip()
        industry = request.form.get("industry", "").strip()

        role_check = f"Role: {role} → It is wrong"
        industry_check = f"Industry: {industry} → Does not fall under the 6 targeted industries"
        final = '<div class="result red">Final: ❌ Red (Not a Match)</div>'

        if role and any(r.lower() == role.lower() for r in TARGET_ROLES):
            role_check = f"Role: {role} → It is correct"
        if industry and any(i.lower() in industry.lower() for i in TARGET_INDUSTRIES):
            industry_check = f"Industry: {industry} → Falls under the 6 targeted industries"

        # ✅ Final Decision
        if "correct" in role_check and "Falls under" in industry_check:
            final = '<div class="result green">Final: ✅ Green (Good Lead)</div>'
        elif "correct" in role_check or "Falls under" in industry_check:
            final = '<div class="result yellow">Final: ⚠️ Yellow (Partial)</div>'

        result_html = f"<p>{role_check}</p><p>{industry_check}</p>{final}"

    return HTML_FORM.format(result=result_html)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
