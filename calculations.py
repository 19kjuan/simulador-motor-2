# calculations.py
import numpy as np

def calculate_horsepower(displacement, boost, efficiency, ecu_mod, exhaust_mod):
    """Calcula la potencia del motor en base a la cilindrada, el aumento de presión, la eficiencia, ECU y modificaciones del escape."""
    base_hp = displacement * 0.1  # Caballos de fuerza base por litro
    boost_hp = base_hp * (boost / 14.7)  # Aumento de presión (boost)
    efficiency_factor = efficiency / 100.0  # Factor de eficiencia
    ecu_factor = 1 + ecu_mod / 100.0  # Factor de ECU
    exhaust_factor = 1 + exhaust_mod / 100.0  # Factor de escape

    total_hp = (base_hp + boost_hp) * efficiency_factor * ecu_factor * exhaust_factor
    return total_hp

def calculate_torque(horsepower, rpm):
    """Calcula el torque del motor en base a la potencia y las revoluciones por minuto."""
    torque = (horsepower * 5252) / rpm
    return torque

def calculate_acceleration(horsepower, weight, gear_ratio):
    """Calcula la aceleración del vehículo en base a la potencia, el peso y la relación de transmisión."""
    power_to_weight_ratio = horsepower / weight
    acceleration = power_to_weight_ratio * gear_ratio * 9.81  # Constante de gravedad
    return acceleration

def calculate_fuel_efficiency(displacement, boost, weight, ecu_mod, exhaust_mod):
    """Calcula la eficiencia de combustible en base a la cilindrada, el aumento de presión, el peso, ECU y modificaciones del escape."""
    base_efficiency = 30.0  # MPG base
    boost_penalty = boost * 0.5  # Penalización por boost
    weight_penalty = weight * 0.02  # Penalización por peso
    ecu_penalty = ecu_mod * 0.1  # Penalización por modificación de ECU
    exhaust_penalty = exhaust_mod * 0.1  # Penalización por modificación de escape

    efficiency = base_efficiency - boost_penalty - weight_penalty - ecu_penalty - exhaust_penalty
    return max(efficiency, 5)  # Eficiencia mínima de 5 MPG
