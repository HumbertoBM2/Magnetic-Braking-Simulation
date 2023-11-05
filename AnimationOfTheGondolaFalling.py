# Programa para hacer una animación que muestre la trayectoria de una imán o góndola en caída libre y que es eventualmente
# frenada por la fuerza magnética generada por un anillo de corriente ubicado en z = 0

# Para el cálculo de la posicion, velocidad y aceleración se utiliza el método numérico Runge-Kutta de cuarto orden 
# Se importan las librerías a utilizar
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 


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
    constantes = (3 * miu0 * I * r**2) / (2 * np.power(d**2 + r**2, 2.5))

     # Vector que almacena la magnitud del campo en el eje z
    Bz = constantes * (deltaz / np.sqrt(d**2 + r**2))

    #Se retorna el vector de campo en z
    return Bz

# Funcion para calcular la magnitud de la fuerza magnética que se ejerce en la góndola mientras cae
# Se parte del supuesto de que la góndola se mueve a través del eje z cuando y = 0
def FuerzaMagnetica(z, r, I, m):
    # Momento dipolar magnético de la góndola 
    miu = 1

    # Permeabilidad del vacío
    miu0 = 4 * np.pi * 1e-7 

    # Cálculo del campo magnético en z
    Bz = CampoMagnetico(0, 0, z, r, I)

    # Cálculo de la fuerza magnética en z
    Fz = ((3 * miu0 * miu * r**2 * I) / 2) * (z / (r**2 + z**2)**(5/2))

    # Se retorna la fuerza magnética 
    return Fz

# Definir parámetros iniciales de la góndola 

# Masa de la góndola 
m = 1e-5

# permeabilidad del vacío 
m0 = 4e-07 * np.pi

# momento dipolar magnético
mu = 1e6

# Radio del anillo
a = 0.08

# Resistencia del material 
R = 9e-5

# Gravedad
g = 9.81

# Fuerza magnética sobre la góndola 
c = (9*(mu*m0)**2*a**4)/(4*R)

# Componente vertical de aceleración 
p = lambda z: z**2/np.sqrt((z**2+a**2)**5)


# Definir las ecuaciones diferenciales
def f(t, y):
    return np.array([y[1], -g - (c/m)*p(y[0]) * y[1]])

# Condiciones iniciales de la simulación 

# Tiempo inicial 
t0 = 0

# Tiempo final 
tf = 10  

# Altura inicial
z0 = 100  

# Velocidad inicial
v0 = 0  

# Paso de tiempo
deltat = 0.01  

# Función para aproximar la velocidad y la posición de la góndola en caída libre usando Runge - Kutta de cuarto orden 
def caidaLibre(f, deltat, x0, y0, xf):

    x = np.arange(x0, xf+deltat, deltat)
    y = np.zeros((len(y0), len(x)))
    y[:, 0] = y0
   
   # Runge - Kutta 
    for i in range(len(x) - 1):

        k1 = f(x[i], y[:, i])
        k2 = f(x[i] + deltat*(1/2), y[:, i] + k1*deltat*(1/2))
        k3 = f(x[i] + deltat*(1/2), y[:, i] + k2*deltat*(1/2))
        k4 = f(x[i] + deltat, y[:, i] + k3*deltat)
        
        next = y[:, i] + (1/6)*deltat*(k1 + 2*k2 + 2*k3 + k4)
        y[:, i+1] = next
        
    # Se retornan los vectores de velocidad y posición ya llenos con Runge - Kutta 
    return x, y

# Se manda llamar la función de Runge - Kutta 
t, y = caidaLibre(f, deltat, t0, np.array([z0, v0]), tf)

# Función para actualizar la animación 
def update(frame):
    # Limpiar la figura actual
    plt.cla() 

    # Dibujar el anillo estático
    plt.plot([0], [0], 'ro', markersize=10) 

    # Dibujar la posición de la góndola 
    plt.plot([0], [y[0, :][frame]], 'bo', markersize=5)  

    # Elementos estéticos de la gráfica 
    plt.xlim([-10, 10])  
    plt.ylim([-10, z0 + 5])  
    plt.xlabel('Posición en x')
    plt.ylabel('Posición en z')
    plt.title('Movimiento de la góndola')
    plt.grid(True)

# Crear la figura y la animación
fig = plt.figure()
ani = FuncAnimation(fig, update, frames=len(t), interval=50)

# Mostrar la animación
plt.show()
