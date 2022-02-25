import numpy as np
import tensorflow.keras.backend as K
import tensorflow as tf

class Genome():
  def __init__(self):
    self.fitness = 0
    self.score = 0
    self.w1 = np.random.randn(3, 10)
    self.w2 = np.random.randn(10, 15)
    self.w3 = np.random.randn(15, 20)
    self.w4 = np.random.randn(20, 10)
    self.w5 = np.random.randn(10, 1)

    self.b1 = np.random.randn(10)
    self.b2 = np.random.randn(15)
    self.b3 = np.random.randn(20)
    self.b4 = np.random.randn(10)
    self.b5 = np.random.randn(1)

  def forward(self, inputs):
    net = np.matmul(inputs, self.w1) + self.b1
    net = tf.keras.activations.relu(net)
  
    net = np.matmul(net, self.w2) + self.b2
    net = tf.keras.activations.sigmoid(net)

    net = np.matmul(net, self.w3) + self.b3
    net = tf.keras.activations.selu(net)

    net = np.matmul(net, self.w4) + self.b4
    net = tf.keras.activations.gelu(net)

    net = np.matmul(net, self.w5) + self.b5
    net = tf.keras.activations.sigmoid(net)
    
    return self.step_function(net)

  def step_function(self, x):
    return np.array(x>0.5, dtype=np.int64)


