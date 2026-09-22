from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def login():
    simulation_triggered = False

    if request.method == "POST":
        # This is only an educational phishing simulation.
        # No username or password is stored or sent anywhere.
        simulation_triggered = True

    return render_template(
        "index.html",
        simulation_triggered=simulation_triggered
    )


if __name__ == "__main__":
    app.run(debug=True)
