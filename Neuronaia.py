import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 59, 72, 100, 100], dtype=float)

# Capas del modelo
oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1], activation='relu')  # Agregado activation='relu'
oculta2 = tf.keras.layers.Dense(units=3, activation='relu')  # Agregado activation='relu'
salida = tf.keras.layers.Dense(units=1)

# Modelo secuencial
modelo = tf.keras.Sequential([oculta1, oculta2, salida])

# Compilación del modelo
modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss="mean_squared_error"
)

# Entrenamiento del modelo
print("Comenzando entrenamiento...")
historia = modelo.fit(celsius, fahrenheit, epochs=1000, verbose=False)
print("Modelo entrenado")

# Visualizar la historia del entrenamiento
plt.plot(historia.history['loss'])
plt.title('Historial del Entrenamiento')
plt.xlabel('Época')
plt.ylabel('Pérdida')
plt.show()

# Hacer una predicción
print("Hagamos una predicción")
resultado = modelo.predict([100.0])
print("El resultado es " + str(resultado[0][0]) + " Fahrenheit!")

# Visualizar las variables internas del modelo
print("Variables internas del modelo")
print("Pesos de la capa oculta 1:")
print(oculta1.get_weights())
print("Pesos de la capa oculta 2:")
print(oculta2.get_weights())
print("Pesos de la capa de salida:")
print(salida.get_weights())
