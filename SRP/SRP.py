class Examination:
	def __init__(self, math, physics):
		self.math = math
		self.physics = physics
		self.maxScore = 200
		
	def calculatePercentage(self):
		print("percentage ", (self.physics + self.math)*100/self.maxScore)

	def printMarksCard(self):
		print(f"marks\n-----\nphysics {self.physics} \n-----\nmath {self.math}")

exam = Examination(50, 80)
exam.calculatePercentage()


exam.printMarksCard()



