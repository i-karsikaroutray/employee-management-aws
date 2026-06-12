from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add-employee")
def add_employee():
    return render_template("add_employee.html")

if __name__ == "__main__":
    app.run(debug=True)
