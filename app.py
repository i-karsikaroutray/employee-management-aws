from flask import Flask, render_template, request

app = Flask(__name__)

employees = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add-employee", methods=["GET", "POST"])
def add_employee():

    if request.method == "POST":

        employee_name = request.form["employee_name"]
        email = request.form["email"]

        employees.append({
            "name": employee_name,
            "email": email
        })

        return "Employee Added Successfully!"

    return render_template("add_employee.html")

@app.route("/view-employees")
def view_employees():
    return render_template(
        "view_employees.html",
        employees=employees
    )    

if __name__ == "__main__":
    app.run(debug=True)
