from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def result():
    try:
        weight = float(request.form["weight"])
        feet = float(request.form["feet"])
        inches = float(request.form["inches"])

        # STEP 1: Convert feet into inches
        total_inches = (feet * 12) + inches

        # STEP 2: Convert total inches into meters
        height_m = total_inches * 0.0254

        bmi = calculate_bmi(weight, height_m)
        category = bmi_category(bmi)

        return render_template("result.html", bmi=bmi, category=category)

    except Exception as e:
        return render_template("result.html", error="Invalid input, please try again!")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
