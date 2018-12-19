import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)  # one_hot [0, 0, 0, ..., 1, ..., 0, 0]

# Input layer
x = tf.placeholder(tf.float32, [None, 784])  # None so that batch size can be changed. 784 for flattened image

# Model node
W = tf.Variable(tf.zeros([784, 10]))  # W = tf.get_variable(name, initializer, ...) is better practice
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W) + b)

# Ground truth
y_ = tf.placeholder(tf.float32, [None, 10])

# Error
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

# Learning rate
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# Session
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

# Train
for _ in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

# Test
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))