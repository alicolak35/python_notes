#https://web.itu.edu.tr/uyar/fad/basics.html

from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)#created an object of Flask class

#whenever there is a request to ".../", the function will be invoked
@app.route("/")#route decorator
def home_page():
    today = datetime.today()
    day = today.strftime("%A")
    return render_template("home_page.html", day=day)

if __name__ == "__main__":
    # host="0.0.0.0": server is publicly available
    # port=8080: server runs on port 8080
    app.run(host="0.0.0.0", port=8080, debug=True)

