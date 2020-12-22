import tensorflow as tf

a = tf.constant(5)
b = tf.constant(4)

c = a * b
print(c)

hello_const = tf.constant("Hello World")
print(hello_const)

# 1 dimensional array
arr = tf.constant([123,345,567])
print(arr)

# 2 dimensional array 

arr2d = tf.constant([[123, 134], [345,456]])
print(arr2d)

