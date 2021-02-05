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

	def update_age(self, new_age):
		self.age = new_age
		print("{} is now {} years old.".format(self.name, self.age))
		self.estimated_insurance_cost()

	def update_num_children(self, new_num_children):
		self.num_of_children = new_num_children
		if self.num_of_children == 1:
			print("{} has {} child.".format(self.name, self.num_of_children))
		else:
			print("{} has {} children.".format(self.name, self,num_of_children))
		self.estimated_insurance_cost()

	def patient_profile(self):
		patient_information = dict(Name = self.name, Age=self.age, Sex = self.sex, BMI = self.bmi, Children = self.num_of_children, Smoker = self.smoker)
		return patient_information

patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
print(patient1.patient_profile())