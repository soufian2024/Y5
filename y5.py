import numpy as np

class f5:
	####################################################
	#                       Loss                       #
	####################################################

	def mse(y_true, y_pred):
		return np.mean(np.power(y_pred - y_true, 2))

	def d_mse(y_true, y_pred):
		return 2 * (y_pred - y_true) / np.size(y_true)





class nn5:


	#####################################################
	#                       Layer                       #
	#####################################################


	class Layer:
		def __init__(self):
			self.input = None
			self.output = None

		def forward(self, input):
			# TODO: return input
			pass

		def backward(self, output_gradient, learning_rate):
			# TODO: update parameters and return input gradient
			pass

	class Dense(Layer):
		def __init__(self,input_size,output_size):
			self.weights = np.random.randn(output_size, input_size)
			self.bias = np.random.randn(output_size,1)

		def forward(self, input):
			self.input = input
			Z = np.dot(self.weights, self.input) + self.bias
			return Z

		def backward(self, output_gradient, learning_rate):
			weights_gradient = np.dot(output_gradient , self.input.T)
			update(weights_gradient,output_gradient)

			output_gradient = np.dot(self.weights.T, output_gradient)
			return output_gradient

		def update(self,weights_gradient,output_gradient):
			self.weights -= learning_rate * weights_gradient
			self.bias -= learning_rate * output_gradient


	####################################################
	#                    Activation                    #
	####################################################


	class Activation(Layer):
		def __init__(self,activation,d_activation):
			self.activation = activation
			self.d_activation = d_activation

		def forward(self, input):
			self.input = input
			a = self.activation(self.input)
			return a

		def backward(self, output_gradient, learning_rate):
			# TODO: update parameters and return input gradient

	class Tanh(Activation):
		def __init__(self):
			tanh = lambda x: np.tanh(x)
			d_tanh = lambda x: 1 - np.tanh(x) ** 2
			super().__init__(tanh, d_tanh)


	


