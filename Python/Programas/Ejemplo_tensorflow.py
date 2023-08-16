import tensorflow as tf

# Datos de entrenamiento
x_train = [1, 2, 3, 4, 8]  
y_train = [0, -1, -2, -3, -1]

# Parámetros del modelo
W = tf.Variable([.3], tf.float32)
b = tf.Variable([-.3], tf.float32)

# Función de modelo
def modelo(X, W, b):
  return W * X + b

# Función de costo  
def costo(y_pred, y_true):
  return tf.reduce_sum(tf.square(y_pred - y_true))

# Optimizador
optimizer = tf.keras.optimizers.SGD(learning_rate=0.01)  

# Entrenamiento
for i in range(1000):
  
  with tf.GradientTape() as tape:
    costo_value = costo(modelo(x_train, W, b), y_train)

  grads = tape.gradient(costo_value, [W, b])  
  optimizer.apply_gradients(zip(grads, [W, b]))

# Evaluar modelo
print(modelo([2], W, b).numpy())