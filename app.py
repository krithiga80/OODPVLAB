from flask import Flask, render_template

app = Flask(__name__)

experiments = [
    {"id": 1, "title": "Experiment 1", "name": "Classes and Objects"},
    {"id": 2, "title": "Experiment 2", "name": "Inheritance"},
    {"id": 3, "title": "Experiment 3", "name": "Polymorphism"},
    {"id": 4, "title": "Experiment 4", "name": "Exception Handling"},
    {"id": 5, "title": "Experiment 5", "name": "File Handling"}
]

@app.route("/experiment/<int:id>")
def experiment(id):
    exp = experiments[id - 1]

    if id == 1:
        return render_template("exp1.html", exp=exp)

    elif id == 2:
        return render_template("exp2.html", exp=exp)

    elif id == 3:
        return render_template("exp3.html", exp=exp)

    elif id == 4:
        return render_template("exp4.html", exp=exp)

    elif id == 5:
        return render_template("exp5.html", exp=exp)