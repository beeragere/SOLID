
class Examination:
	def __init__(self, math, physics):
		self.math = math
		self.physics = physics
		self.maxScore = 200
		
	def calculatePercentage(self):
		print("percentage ", (self.physics + self.math)*100/self.maxScore)



class Printer:
	def printMarksCard(self, marks):
		print(f"marks\n-----\nphysics {marks.get('physics')} \n-----\nmath {marks['math']}")

exam = Examination(50, 80)
exam.calculatePercentage()

printer = Printer()

printer.printMarksCard({"physics": exam.physics, "math": exam.math})





