from flask import Flask, request, render_template

app = Flask(__name__)

def calculate_dose(weight, dose_per_kg):
    return weight * dose_per_kg

def calculate_volume(dose, concentration_mg, concentration_ml):
    concentration = concentration_mg / concentration_ml  # Konsantrasyonu mg/ml olarak hesapla
    return dose / concentration

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        weight_unit = request.form['weight_unit']
        dose_per_kg = float(request.form['dose_per_kg'])
        concentration_mg = float(request.form['concentration_mg'])
        concentration_ml = float(request.form['concentration_ml'])

        if weight_unit == 'gram':
            weight /= 1000.0  # Gramdan kg'a çevir

        weight_based_dose = calculate_dose(weight, dose_per_kg)
        volume = calculate_volume(weight_based_dose, concentration_mg, concentration_ml)

        return render_template('index.html', weight_based_dose=weight_based_dose, volume=volume)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
