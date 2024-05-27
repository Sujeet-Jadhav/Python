class Honda:
	# First we create a constructor for this class
	# and add members to it, here models
	def __init__(self):
		self.models = ['City', 'Accord', 'Civic', 'Amaze']

	def outModels(self):
		print('These are the available models for Honda')
		for model in self.models:
			print('\t%s ' % model)
