from flask import Flask
from flask import render_template
from flask import send_file

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("demo.html")

if __name__ == "__main__":
    app.run(port=6666, host='0.0.0.0', debug=True)