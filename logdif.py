import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Variables de entrada
temperatura = ctrl.Antecedent(np.arange(15, 36, 1), 'temperatura')
ocupacion = ctrl.Antecedent(np.arange(0, 11, 1), 'ocupacion')

# Variable de salida
enfriamiento = ctrl.Consequent(np.arange(0, 101, 1), 'enfriamiento')

# Funciones de membresía para temperatura
temperatura['baja'] = fuzz.trimf(temperatura.universe, [15, 15, 22])
temperatura['media'] = fuzz.trimf(temperatura.universe, [20, 25, 28])
temperatura['alta'] = fuzz.trimf(temperatura.universe, [26, 35, 35])


# Funciones de membresía para ocupación
ocupacion['baja'] = fuzz.trimf(ocupacion.universe, [0, 0, 5])
ocupacion['media'] = fuzz.trimf(ocupacion.universe, [3, 5, 7])
ocupacion['alta'] = fuzz.trimf(ocupacion.universe, [5, 10, 10])

# Funciones de membresía para enfriamiento
enfriamiento['muy_bajo'] = fuzz.trimf(enfriamiento.universe, [0, 0, 25])
enfriamiento['bajo'] = fuzz.trimf(enfriamiento.universe, [0, 25, 50])
enfriamiento['medio'] = fuzz.trimf(enfriamiento.universe, [25, 50, 75])
enfriamiento['alto'] = fuzz.trimf(enfriamiento.universe, [50, 75, 100])
enfriamiento['muy_alto'] = fuzz.trimf(enfriamiento.universe, [75, 100, 100])

#definir reglas
#Si la temperatura es alta y la ocupación es alta, entonces el nivel de enfriamiento debe ser alto
rule1 = ctrl.Rule(temperatura['alta'] & ocupacion['alta'], enfriamiento['alto'])

#si la temperatura es alta y la ocupación es baja, entonces el nivel de enfriamiento debe ser medio
rule2 = ctrl.Rule(temperatura['alta'] & ocupacion['baja'], enfriamiento['medio'])

#Si la temperatura es media y la ocupacion alta, entonces el enfriamiento es medio
rule3 = ctrl.Rule(temperatura['media'] & ocupacion['alta'], enfriamiento['medio'])

#Si la temperatura es media y la ocupacion baja, entonces el enfriamiento es alto
rule4 = ctrl.Rule(temperatura['media'] & ocupacion['baja'], enfriamiento['alto'])

#Si la temperatura es baja y la ocupación es alta, entonces el nivel de enfriamiento debe ser bajo
rule5 = ctrl.Rule(temperatura['baja'] & ocupacion['alta'], enfriamiento['bajo'])

#Si la temperatura es baja y la ocupación es baja, entonces el nivel de enfriamiento debe ser muy bajo o apagado
rule6 = ctrl.Rule(temperatura['baja'] & ocupacion['baja'], enfriamiento['bajo'])


temperatura.view()
ocupacion.view()
enfriamiento.view()
plt.show()