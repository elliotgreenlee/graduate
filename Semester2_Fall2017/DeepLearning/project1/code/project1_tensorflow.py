# Vary: learning rate: 0.00001, 0.0001, 0.001, 0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 100.0
# Vary: batch size: 10, 50, 100, 200, 1000, 5000, 10000, 20000
# Vary: iterations: 1, 10, 100, 1000, 2000, 5000, 10000
# Vary: activation function: see below
# Vary: number nodes in a layer 8, 16, 32, 64, 128, 256, 512, 1024, 2048
# Vary: number of hidden layers: 1, 2, 4, 8

# Evaluation on accuracy, convergence speed: plotting the error or accuracy, runtime

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)


class Network(object):
    def __init__(self, learning_rate, iterations, batch_size, layers):
        self.lr = learning_rate
        self.iterations = iterations
        self.batch_size = batch_size
        self.layers = layers
        self.build_graph()

    def activation_function(self, x):
        return tf.nn.sigmoid(x)
        # return tf.nn.tanh(x)
        # return tf.nn.elu(x)
        # return tf.nn.softplus(x)
        # return tf.nn.relu(x)

    def build_layer(self, input_size, output_size, x):
        W = tf.Variable(tf.truncated_normal([input_size, output_size], stddev=1))
        b = tf.Variable(tf.truncated_normal([output_size], stddev=1))
        return self.activation_function(tf.matmul(x, W) + b)

    def build_graph(self):

        self.x = tf.placeholder(tf.float32, [None, 784])

        layer_ = []
        layer_.append(self.build_layer(784, 30, self.x))

        for layer in range(1, self.layers):
            layer_.append(self.build_layer(30, 30, layer_[layer-1]))

        print(len(layer_))

        W = tf.Variable(tf.truncated_normal([30, 10], stddev=1))
        b = tf.Variable(tf.truncated_normal([10], stddev=1))
        self.y = tf.nn.softmax(tf.matmul(layer_[-1], W) + b)


        self.y_ = tf.placeholder(tf.float32, [None, 10])
        self.cross_entropy = tf.reduce_mean(-tf.reduce_sum(self.y_ * tf.log(self.y), reduction_indices=[1]))
        self.train_step = tf.train.GradientDescentOptimizer(self.lr).minimize(self.cross_entropy)

        self.correct_prediction = tf.equal(tf.argmax(self.y, 1), tf.argmax(self.y_, 1))
        self.accuracy = tf.reduce_mean(tf.cast(self.correct_prediction, tf.float32))

    def train(self):
        xs = []
        t_accs = []

        self.sess = tf.Session()
        init = tf.global_variables_initializer()
        self.sess.run(init)
        for i in range(self.iterations):
            batch_xs, batch_ys = mnist.train.next_batch(self.batch_size)
            _, accuracy = self.sess.run([self.train_step, self.accuracy], feed_dict={self.x: batch_xs, self.y_: batch_ys})
            xs.append(i)
            t_accs.append(accuracy)
        return xs, t_accs

    def eval(self):
        self.correct_prediction = tf.equal(tf.argmax(self.y, 1), tf.argmax(self.y_, 1))
        accuracy = tf.reduce_mean(tf.cast(self.correct_prediction, tf.float32))
        return self.sess.run(accuracy, feed_dict={self.x: mnist.test.images, self.y_: mnist.test.labels})


if __name__ == "__main__":
    ins = [1, 2, 4]
    accs = []
    plt.figure(2)
    for i, layers in enumerate(ins):
        p = Network(0.01, 10000, 100, layers)
        xs, t_accs = p.train()
        plt.subplot(310 + i)
        #print(i, t_accs)
        plt.plot(xs, t_accs)
        print(layers)
        accs.append(p.eval())

    plt.ylabel("Accuracy")
    plt.show()

    plt.figure(1)
    plt.plot(ins, accs, 'ro')
    plt.axis([0, 4, 0, 1.0])
    plt.ylabel("Accuracy")
    plt.xlabel("Hidden Layers")
    plt.show()

