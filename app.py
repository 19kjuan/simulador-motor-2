from flask import Flask, render_template, request, jsonify
from calculations import calculate_horsepower, calculate_torque, calculate_acceleration, calculate_fuel_efficiency

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        displacement = float(request.form['displacement'])
        boost = float(request.form['boost'])
        efficiency = float(request.form['efficiency'])
        rpm = float(request.form['rpm'])
        weight = float(request.form['weight'])
        ecu_mod = float(request.form['ecu_mod'])
        exhaust_mod = float(request.form['exhaust_mod'])
        gear_ratio = float(request.form['gear_ratio'])

        horsepower = calculate_horsepower(displacement, boost, efficiency, ecu_mod, exhaust_mod)
        torque = calculate_torque(horsepower, rpm)
        acceleration = calculate_acceleration(horsepower, weight, gear_ratio)
        fuel_efficiency = calculate_fuel_efficiency(displacement, boost, weight, ecu_mod, exhaust_mod)

        return jsonify({
            'horsepower': horsepower,
            'torque': torque,
            'acceleration': acceleration,
            'fuel_efficiency': fuel_efficiency
        })

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

