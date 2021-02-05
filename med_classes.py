class Patient:
	def __init__(self, name, age, sex, bmi, num_of_children, smoker):
	    self.name = name
	    self.age = age
	    # add more parameters here
	    self.sex = sex
	    self.bmi = bmi
	    self.num_of_children = num_of_children
	    self.smoker = smoker

	def estimated_insurance_cost(self):
		estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
		print("{}'s estimated insurance cost is {} dollars.".format(self.name, estimated_cost))

patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
patient1.estimated_insurance_cost()