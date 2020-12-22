import tensorflow as tf

string = tf.Variable("This is a string", tf.string)
print(string.shape)


tensor1 = tf.ones([1,2,3])
print(tensor1)

t = tf.zeros([5,5,5,5])

t = tf.reshape(t,[25,-1])

print(t)
