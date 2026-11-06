from flask import Flask, render_template

app = Flask(__name__)

# Placeholder voor database (week 3)
# Hier komt later de koppeling met de SQL-database.


@app.route("/")
def hello_world():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
