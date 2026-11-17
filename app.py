
from flask import Flask, render_template, request

app = Flask(__name__)


# Electricity Bill Calculation
def calculate_bill(units):

    if units < 0:
        raise ValueError("Units cannot be negative")

    if units <= 100:
        bill = units * 1.50

    elif units <= 200:
        bill = (100 * 1.50) + ((units - 100) * 2.50)

    elif units <= 300:
        bill = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)

    else:
        bill = (
            (100 * 1.50)
            + (100 * 2.50)
            + (100 * 4.00)
            + ((units - 300) * 6.00)
        )

    return bill


# Homepage
@app.route("/", methods=["GET", "POST"])
def home():

    bill = None
    units = ""
    error = None

    if request.method == "POST":

        try:
            units = request.form.get("units", "").strip()

            if not units:
                raise ValueError("Please enter electricity units")

            units_value = float(units)

            if not units_value.is_integer():
                raise ValueError("Please enter whole units")

            units_value = int(units_value)

            bill = calculate_bill(units_value)

        except ValueError as e:
            error = str(e)

    return render_template(
        "index.html",
        bill=bill,
        units=units,
        error=error
    )


# Run Flask Application
if __name__ == "__main__":

    print("Electricity Bill Calculator")
    print("Open: http://192.168.1.41:5000")

    app.run(
        host="192.168.1.41",
        port=5000,
        debug=True,
        use_reloader=False
    )
