from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add-employee", methods=["GET", "POST"])
def add_employee():

    if request.method == "POST":

        employee_name = request.form["employee_name"]
        email = request.form["email"]

        return f"""
        Employee Added Successfully!<br><br>
        Name: {employee_name}<br>
        Email: {email}
        """

    return render_template("add_employee.html")

if __name__ == "__main__":
    app.run(debug=True)
