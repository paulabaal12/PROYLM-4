import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Variables de entrada
temperatura = ctrl.Antecedent(np.arange(15, 36, 1), 'temperatura')
ocupacion = ctrl.Antecedent(np.arange(0, 11, 1), 'ocupacion')

# Variable de salida
enfriamiento = ctrl.Consequent(np.arange(0, 101, 1), 'enfriamiento')