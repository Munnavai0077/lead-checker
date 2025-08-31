from flask import Flask, request

app = Flask(__name__)

# --- Configure your matching here (simple demo lists; expand any time) ---
TARGET_ROLES = {
    "chief operating officer",
    "director application development",
    "software test manager",
    "director of engineering",
    "head of machine learning",
    "vice president of engineering",
    "director quality engineering",
}
TARGET_INDUSTRIES = [
    "saas", "technology & it services", "cloud", "enterprise software",
    "ai", "machine learning", "automation", "digital transformation",
    "consulting", "b2b software", "enterprise applications"
]
# -------------------------------------------------------------------------


HTML_FORM = """
<!doctype html>
<html>
<head>
  <meta charset="utf-8"/>
  <title>Lead Checker</title>
  <style>
    /* Red–white “industrial” diagonal stripes */
    body{
      margin:0;
      min-height:100vh;
      display:flex;
      align-items:center;
      justify-content:center;
      font-family:Arial, Helvetica, sans-serif;
      background:
        repeating-linear-gradient(
          45deg,
          #d90429 0 24px,   /* red */
          #ffffff 24px 48px /* white */
        );
    }

    /* Dim overlay so the card pops */
    .overlay{
      position:fixed; inset:0;
      background:rgba(255,255,255,.35);
      pointer-events:none;
    }

    /* Center card */
    .card{
      position:relative;
      width: min(92vw, 520px);
      background:#fff;
      border-radius:14px;
      box-shadow:0 18px 40px rgba(0,0,0,.18);
      padding:28px 26px 24px;
      z-index:1;
    }

    h1{
      margin:0 0 14px;
      font-size:26px; letter-spacing:.4px; color:#111827;
      text-align:center;
    }
    p.sub{
      margin:0 0 18px; text-align:center; color:#6b7280; font-size:13px;
    }

    label{display:block; font-weight:600; color:#374151; margin:10px 0 6px;}
    input[type=text]{
      width:100%;
      padding:12px 14px;
      border:1px solid #d1d5db;
      border-radius:10px;
      outline:none;
      transition:border .15s, box-shadow .15s;
      font-size:14px;
      background:#f9fafb;
    }
    input[type=text]:focus{
      border-color:#3b82f6;
      box-shadow:0 0 0 3px rgba(59,130,246,.15);
      background:#fff;
    }

    .actions{
      display:flex; gap:10px; justify-content:center; margin-top:16px;
    }
    button{
      border:0; cursor:pointer;
      padding:11px 18px; border-radius:10px;
      font-weight:700; letter-spacing:.2px;
      color:#fff; background:#2563eb;      /* blue */
      transition:transform .04s ease, filter .15s ease;
    }
    button:hover{ filter:brightness(.96); }
    button:active{ transform:translateY(1px); }

    /* Result boxes */
    .result{ margin-top:18px; display:grid; gap:10px; }
    .pill{
      border-radius:12px; padding:12px 14px; font-weight:600; line-height:1.35;
      border:1px solid transparent;
    }
    .green{ background:#e8f8ee; border-color:#b7efc5; color:#0f7a3d; }
    .yellow{ background:#fff7df; border-color:#ffe6a7; color:#996c00; }
    .red{ background:#ffe8e8; border-color:#ffb4b4; color:#a11919; }

    .mono{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; }
  </style>
</head>
<body>
  <div class="overlay"></div>
  <div class="card">
    <h1>Lead Classification</h1>
    <p class="sub">Enter a role and/or company/industry info</p>

    <form method="POST" autocomplete="off">
      <label for="role">Role</label>
      <input id="role" name="role" type="text" placeholder="e.g., Chief Operating Officer" />

      <label for="industry">Industry / Company Info</label>
      <input id="industry" name="industry" type="text" placeholder="e.g., SaaS, AI, Cloud" />

      <div class="actions">
        <button type="submit">Check</button>
      </div>
    </form>

    {RESULT_BOXES}
  </div>
</body>
</html>
"""

def classify(role: str, industry: str):
    """Return (role_line, industry_line, final_text, final_color) based on inputs."""
    role_line = None
    industry_line = None
    final_text, final_color = "Final: ❌ Red (Not a Match)", "red"

    role = (role or "").strip()
    industry = (industry or "").strip()

    # Role check only if provided
    if role:
        ok_role = role.lower() in TARGET_ROLES
        role_line = f"Role: {role} → {'It is correct' if ok_role else 'It is wrong'}"
    else:
        ok_role = False

    # Industry check only if provided
    if industry:
        ok_ind = any(term in industry.lower() for term in TARGET_INDUSTRIES)
        industry_line = f"Industry: {industry} → {'Falls under the 6 targeted industries' if ok_ind else 'Does not fall under the 6 targeted industries'}"
    else:
        ok_ind = False

    # Final decision
    if ok_role and ok_ind:
        final_text, final_color = "Final: ✅ Green (Good Lead)", "green"
    elif ok_role or ok_ind:
        final_text, final_color = "Final: ⚠️ Yellow (Partial)", "yellow"

    return role_line, industry_line, final_text, final_color


@app.route("/", methods=["GET", "POST"])
def home():
    result_html = ""
    if request.method == "POST":
        role = request.form.get("role", "")
        industry = request.form.get("industry", "")

        role_line, ind_line, final_text, final_color = classify(role, industry)

        boxes = []
        if role_line: boxes.append(f'<div class="pill mono { "green" if "correct" in role_line else "red" }">{role_line}</div>')
        if ind_line: boxes.append(f'<div class="pill mono { "green" if "Falls under" in ind_line else "red" }">{ind_line}</div>')
        boxes.append(f'<div class="pill {final_color} mono">{final_text}</div>')

        result_html = '<div class="result">' + "".join(boxes) + "</div>"

    return HTML_FORM.replace("{RESULT_BOXES}", result_html)


if __name__ == "__main__":
    # For local testing; Render will run with gunicorn app:app
    app.run(host="0.0.0.0", port=5000)
