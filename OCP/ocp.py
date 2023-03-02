
class Guitar:
	def __init__(self, stringCount, tuning, action, gauge):
		self.stringCount = stringCount
		self.tuning = tuning
		self.action = action
		self.stringGauge = gauge
		
	def guitarInfo(self):
		print("num of strings ", self.stringCount, " tuning ", self.tuning)

	# def checkIfElectric(self):
	# 	if(self.action < 2 and self.stringGauge < 0.4):
	# 		print("the guitar is electric")



guitar = Guitar("6", "EADGBE", 1.3, 0.1)
guitar.guitarInfo()


# guitar.checkIfElectric()
