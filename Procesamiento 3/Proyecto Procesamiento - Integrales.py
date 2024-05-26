import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# data is read from excel file
archivo_excel = 'Datos.xlsx'
df = pd.read_excel(archivo_excel)

# Save the data from the 'Stress' and 'Strain' columns
esfuerzo = df['Esfuerzo'].values
deformacion = df['Deformación'].values

# Function to adjust the number of points
def ajustar_puntos(x, y):
    n = len(x)
    while (n - 1) % 3 != 0 or n % 2 == 0:
        n -= 1
    return x[:n], y[:n]

# Adjust data to meet method requirements
deformacion, esfuerzo = ajustar_puntos(deformacion, esfuerzo)

# Plot of fitted data
plt.figure(figsize=(10, 6))
plt.plot(deformacion, esfuerzo, 'bo-', label='Experimental data')
plt.fill_between(deformacion, esfuerzo, color='skyblue', alpha=0.4)
plt.xlabel('Strain')
plt.ylabel('Stress [MPa]')
plt.title('Stress-Strain Curve of 1045 Steel')
plt.legend()
plt.grid(True)
plt.show()


# Functions for calculating areas under the curve

def metodo_trapecio(x, y):
    n = len(x) - 1
    area = 0.0
    for i in range(n):
        area += (x[i+1] - x[i]) * (y[i] + y[i+1]) / 2
    return area

def metodo_simpson_1_3(x, y):
    n = len(x) - 1
    h = (x[-1] - x[0]) / n
    area = y[0] + y[-1]
    for i in range(1, n, 2):
        area += 4 * y[i]
    for i in range(2, n-1, 2):
        area += 2 * y[i]
    area *= h / 3
    return area

def metodo_simpson_3_8(x, y):
    n = len(x) - 1
    h = (x[-1] - x[0]) / n
    area = y[0] + y[-1]
    for i in range(1, n, 3):
        area += 3 * y[i]
    for i in range(2, n, 3):
        area += 3 * y[i]
    for i in range(3, n-1, 3):
        area += 2 * y[i]
    area *= 3 * h / 8
    return area


# calculate area under the curve

print("RESULTS")

area_trapecio = metodo_trapecio(deformacion, esfuerzo)
print(f"Toughness by the multiple trapezoid method [MJ/m3]: {area_trapecio:.4f}")

area_simpson_1_3 = metodo_simpson_1_3(deformacion, esfuerzo)
print(f"Toughness by Simpson's method 1/3 [MJ/m3]: {area_simpson_1_3:.4f}")

area_simpson_3_8 = metodo_simpson_3_8(deformacion, esfuerzo)
print(f"Toughness by Simpson method 3/8 [MJ/m3]: {area_simpson_3_8:.4f}")