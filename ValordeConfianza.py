import numpy as np #np is the standar name for numpy
import scipy.stats as st #st is the standar name for spicy.stats

#Data set to work with
datos = [12, 12, 13, 13, 15, 16, 17, 22, 23, 25, 26, 27, 28, 28, 29]

intervalo_confianza = st.t.interval(alpha = 0.95, df = len(datos) - 1, loc = np.mean(datos), scale = st.sem(datos))

print("El valor de confianza del 95% es: ", intervalo_confianza)
