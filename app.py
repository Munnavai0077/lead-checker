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
        h1 {
            margin-bottom: 20px;
            color: #333;
        }
        label {
            display: block;
            text-align: left;
            margin: 10px 0 5px;
            font-weight: bold;
        }
        input[type=text] {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 6px;
        }
        input[type=submit] {
            padding: 10px 20px;
            background: #007BFF;
            border: none;
            color: white;
            border-radius: 6px;
            cursor: pointer;
        }
        input[type=submit]:hover {
            background: #0056b3;
        }
        .result {
            margin-top: 20px;
            font-size: 14px;
            color: #444;
            text-align: left;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Lead Classification</h1>
        <form method="post">
            <label>Role:</label>
            <input type="text" name="role">
            
            <label>Industry/Company Info:</label>
            <input type="text" name="industry">
            
            <input type="submit" value="Check">
        </form>
    </div>
</body>
</html>
"""
