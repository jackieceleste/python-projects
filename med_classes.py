class Patient:
  def __init__(self, name, age, sex, bmi, num_of_children, smoker):
    self.name = name
    self.age = age
    # add more parameters here
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker = smoker

patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
print(patient1.name, patient1.age, patient1.sex, patient1.bmi, patient1.num_of_children, patient1.smoker)