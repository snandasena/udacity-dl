import tensorflow as tf


def get_weights(n_features, n_labels):

    return tf.Variable(tf.random.truncated_normal((n_features, n_labels)))


def get_biases(n_labels):
    
    return tf.Variable(tf.zeros(n_labels))

def linear(inpt, w,b):

    return tf.add(tf.matmul(inpt, w), b)



