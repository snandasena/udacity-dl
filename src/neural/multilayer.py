import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Network size
N_input = 4
N_hidden = 3
N_output = 2

np.random.seed(42)

X = np.random.randn(4)

weigts_input_to_hidden = np.random.normal(0, scale=0.1, size=(N_input, N_hidden))
weights_input_to_output = np.random.normal(0, scale=0.2, size=(N_hidden, N_output))

hidden_layer_in =   np.dot(X, weigts_input_to_hidden)
hidden_layer_out = sigmoid(hidden_layer_in)

print("Hidden layer output: ", hidden_layer_out)

output_layer_in = np.dot(hidden_layer_out, weights_input_to_output)
output_layer_out = sigmoid(output_layer_in)

print("Output layer output: ", output_layer_out)

