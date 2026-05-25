from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# HTML Content for the beginner-friendly login webpage
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head><title>QA Practice Login</title></head>
<body style="font-family: Arial; margin: 40px;">
    <h2>QA Test Login Page</h2>
    <form action="/api/login" method="POST">
        <label>Username:</label><br>
        <input type="text" name="username" value="qa_user"><br><br>
        <label>Password:</label><br>
        <input type="password" name="password" value="password123"><br><br>
        <button type="submit">Submit (Triggers POST)</button>
    </form>
</body>
</html>
"""

# Route 1: Displays the actual UI webpage (GET request)
@app.route('/', methods=['GET'])
def home():
    return render_template_string(HTML_PAGE)

# Route 2: The actual backend API Endpoint (POST request)
@app.route('/api/login', methods=['POST'])
def api_login():
    # Handle incoming JSON from Postman OR standard Form data from the browser
    data = request.get_json(silent=True) or request.form
    
    username = data.get("username")
    password = data.get("password")

    # Beginner validation logic
    if username == "qa_user" and password == "password123":
        return jsonify({
            "status": "success",
            "message": "Authentication successful!",
            "token": "QA_SESSION_TOKEN_ABC123"
        }), 200 # 200 OK Status Code
    else:
        return jsonify({
            "status": "error",
            "message": "Invalid username or password"
        }), 401 # 401 Unauthorized Status Code

if __name__ == '__main__':
    print(" Server running! Open http://127.0.0.1:5000 in your browser.")
    app.run(port=5000, debug=True)
