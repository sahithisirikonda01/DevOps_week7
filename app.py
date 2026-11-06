from flask import Flask, request, render_template_string

app = Flask(__name__)

users = []

html = """
<!DOCTYPE html>
<html>
<head>
    <title>User Registration</title>
</head>
<body>
    <h2>User Registration Form</h2>

    <form method="POST">
        <label>Name:</label>
        <input type="text" name="name" required><br><br>

        <label>Email:</label>
        <input type="email" name="email" required><br><br>

        <label>Password:</label>
        <input type="password" name="password" required><br><br>

        <button type="submit">Register</button>
    </form>

    <h3>{{ message }}</h3>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def register():
    message = ""

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]

        users.append({"name": name, "email": email})
        message = "Registration successful! Welcome " + name

    return render_template_string(html, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)