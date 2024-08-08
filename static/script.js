document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('modForm');
    const resultsDiv = document.getElementById('results');
    const resultHorsepower = document.getElementById('resultHorsepower');
    const resultTorque = document.getElementById('resultTorque');
    const resultAcceleration = document.getElementById('resultAcceleration');
    const resultFuelEfficiency = document.getElementById('resultFuelEfficiency');

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        const formData = new FormData(form);

        fetch('/', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            resultHorsepower.textContent = data.horsepower.toFixed(2);
            resultTorque.textContent = data.torque.toFixed(2);
            resultAcceleration.textContent = data.acceleration.toFixed(2);
            resultFuelEfficiency.textContent = data.fuel_efficiency.toFixed(2);
            resultsDiv.style.display = 'block';
        })
        .catch(error => console.error('Error:', error));
    });
});
