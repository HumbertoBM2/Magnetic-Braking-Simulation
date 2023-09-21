# Programa para generar las líneas de campo magnético de un anillo cargado 

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

# Se define la función de aproximaciones númericas que se usará para corrroborar que los resultados obtenidos son correctos
def aproximacionNumericaCampo(x, y, z, r, I):
  # Permeabilidad del vacío
  miu0aprox = 4 * np.pi * 1e-7

  # Calculo de los campos en y y z cuando el punto tiene coordenada en y = 0
  if y == 0:
    d = np.sqrt(r**2 + z**2)
    Bz = (1/2) * miu0aprox * r**2 * I / (d**3)
    By = 0

  # Calculo de los campos en y y z usando aproximaciones numericas 
  else:

    d = np.sqrt(y**2 + z**2)
    By = (3/2) * miu0aprox * r**2 * I * (y * z) / (d**5)
    Bz = (1/2) * miu0aprox * r**2 * I * (1 / d**3) * (1 - (3 * y**2) / (d**2))

  return By, Bz



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

# Magnitud del campo magnético
B = np.sqrt(Bx**2 + By**2 + Bz**2) 

# Graficar las líneas de campo en el plano yz con la función streamplot
plt.streamplot(y, z, By, Bz, density = 1.5, color ='blue', linewidth = 1, arrowstyle = '->', arrowsize = 1)

# Mapa de calor 
plt.contourf(y, z, B, levels = 20, cmap ='hot')

# Graficar el anillo dentro de la malla
AnguloAnillo = np.linspace(0, 2 *np.pi, 100)
AnilloX = r * np.cos(AnguloAnillo)
AnilloY = r * np.sin(AnguloAnillo)
AnilloZ = np.zeros_like(AnguloAnillo)
plt.plot(AnilloY, AnilloZ, color = 'green', linewidth = 7)

# Titulos de la gráfica 
plt.xlabel ('Eje y')
plt.ylabel ('Eje z')
plt.title ('Líneas de campo magnético debido a un anillo cargado')
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.gca().set_aspect('equal')
cbar = plt.colorbar(label ='Magnitud del campo magnético')
cbar.set_label('Magnitud del campo magnético', rotation = 270, labelpad = 15)


# Seleccionar un punto aleatorio lejos del anillo 
pRandomY = np.random.uniform(-100, 100)
pRandomZ = np.random.uniform(-100, 100)

# Comparación entre el resultado exacto con Biot Savart y las aproximaciones numéricas 

# Calculo exacto de campo con Biot - Savart en el punto aleatorio
Bx_BS, By_BS, Bz_BS = CampoMagnetico(0, pRandomY, pRandomZ, r, I)
CampoBSExacto = np.sqrt(Bx_BS**2 + By_BS**2 + Bz_BS**2)

# Calculo del campo con aproximaciones numéricas en el punto aleatorio 
By_AN, Bz_AN = aproximacionNumericaCampo(0, pRandomY, pRandomZ, r, I)
CampoAN = np.sqrt(By_AN**2 + Bz_AN**2)

# Comparación de resultados y cálculo del error aproximado 
error = np.abs(CampoBSExacto - CampoAN)
print(f'Magnitud del campo Biot-Savart: {CampoBSExacto} T')
print(f'Magnitud del campo con aproximacion numerica: {CampoAN} T')
print(f'Error aproximado: {error}')

# Se declara la tolerancia y se corrobora que el error obtenido entre en el margen de tolerancia 
tolerancia = (1*10**(-5))
if error < tolerancia:
  print("El calculo con Biot-Savart fue correcto")
else:
  print("El calculo con Biot-Savart fue incorrecto")

# Imprimir resultados 
plt.show()