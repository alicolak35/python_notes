from flask import Flask, render_template, request
"""
HTTP methods;
GET: retrieves data from server
POST; sends data to server
PUT: updates an existing source
DELETE: deletes a resource
PATCH: partially updates a resource
"""
app = Flask(__name__)

@app.route("/about")
def about():
    return "About page"

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    username = request.values.get("username")
    return f"Welcome, {username}"
if __name__ == '__main__':
    app.run(debug=True)#Debug mode causes security problems. Therefore this mode should be enabled only during development.