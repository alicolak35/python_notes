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
def form():
    return render_template("home.html")

@app.route("/age", methods=["POST"])
def form_age():
    return render_template("age.html")

@app.route("/print", methods=["POST"])
def print_out():
    age = request.form["age"]#get("age")
    username = request.form["username"]
    return f"So {username}, you are {age} years old ha!" 


if __name__ == '__main__':
    app.run(debug=True)#Debug mode causes security problems. Therefore this mode should be enabled only during development.


