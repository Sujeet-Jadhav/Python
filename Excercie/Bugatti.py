class Bugatti:
	# First we create a constructor for this class
	# and add members to it, here models
	def __init__(self):
		self.models = ['Chiron', 'Veyron', 'Divo', 'Centodieci']

	# A normal print function
	def outModels(self):
		print('These are the available models for Bugatti')
		for model in self.models:
			print(model)
