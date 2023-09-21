# Programa para comparar los valores de campo en cada componente del campo magnético generado por un anillo cargado 
# Se usa la ley de Biot-Savart 
# Se importan librerías a utilizar para el dibujo de las líneas de campo 
import numpy as np
import matplotlib.pyplot as plt

# Se define la función para el calculo del campo eléctrico usando la ley de Biot-Savart
def CampoMagnetico(x, y, z, r, I):

  # Permeabilidad del vacío 
  miu0 = 4 * np.pi * 1e-7    

  # Vectores que almacenan la diferencia entre las coordenadas del punto en el que se está calculando el campo y el punto del anillo con el que se esté trabajando
  deltax = x
  deltay = y
  deltaz = z

  # Distancia entre el punto a trabajar y el anillo 
  d = np.sqrt(deltax**2 + deltay**2 + deltaz**2) 

  # Valores constantes de la integral
  constantes = miu0 * I * r**2 / (np.power(d**2 + r**2, 1.5))  

  # Vectores que almacenan los componentes del campo magnético 
  Bx = constantes * (3 * deltax * deltaz) 
  By = constantes * (3 * deltay * deltaz)
  Bz = constantes * (3 * deltaz**2 - d**2)

  # Se retornan los vectores de campo
  return Bx, By, Bz  

# Main

# Definición de los parámetros iniciales del anillo 

# Radio del anillo 
r = 1

# Corriente a tráves del anillo 
I = 1

# Creación de las mallas donde se graficará el campo por medio de vectores
y , z = np.meshgrid(np.linspace(-6, 6, 100), np.linspace(-6, 6, 100))
x = np.zeros_like(y)

# Calculo del campo magnético en todos los puntos de la malla mediante la función creada
Bx, By, Bz = CampoMagnetico(x, y, z, r, I)

# Crear una gráfica que compare los valores de cada componente del campo magnético generado por el anillo cargado
plt.plot(y[:, 0], Bx[:, 0], 'o-', label = 'Bx')
plt.plot(y[:, 0], By[:, 0], 's-', label = 'By')
plt.plot(y[:, 0], Bz[:, 0], '^-', label = 'Bz')
plt.axhline(y = 0, color = 'gray', linestyle = '--')
plt.xlabel('')
plt.ylabel('Campo Magnético')
plt.title('Comparación de campo magnético entre cada componente')
plt.legend()

# Imprimir resultados 
plt.show()