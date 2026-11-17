class Patient:
  def __init__(self, name : str, bill_amount : float):
    self.__name = name
    self.__bill_amount = bill_amount

  def get_name(self):
    return self.__name

  def set_name(self,name):
    self.__name = str(name)

  def get_bill_amount(self):
    return self.__bill_amount

  def set_bill_amount(self,bill_amount):
    self.__bill_amount = float(bill_amount)

  def calculate_bill(self):
    print("Original Bill:", "₱", self.get_bill_amount())
    print("Final Bill:", "₱", self.get_bill_amount())

  def display_patient_type(self):
    print("Regular Patient")

class Senior(Patient):
  def __init__(self,name : str, bill_amount : float):
    super().__init__(name, bill_amount)

  def calculate_bill(self):
          #20% discount
    print("Original Bill:", "₱", self.get_bill_amount())
    discount = self.get_bill_amount() * 0.20
    total_bill = self.get_bill_amount() - discount
    self.set_bill_amount(total_bill)
    print("Final Bill:", "₱", self.get_bill_amount())

  def display_patient_type(self):
    print("Senior Citizen")

class PhilHealth(Patient):
  def __init__(self, name : str, bill_amount : float):
    super().__init__(name, bill_amount)
    
  def calculate_bill(self):
      #15% discount
    print("Original Bill:", "₱", self.get_bill_amount())
    discount = self.get_bill_amount() * 0.15
    total_bill = self.get_bill_amount() - discount
    self.set_bill_amount(total_bill)
    print("Final Bill:", "₱", self.get_bill_amount())

  def display_patient_type(self):
    print("PhilHealth Member")

patient1 = Patient("Juan Dela Cruz", 15000)
patient2 = Senior("Maria Santos", 15000)
patient3 = PhilHealth("Pedro Reyes", 15000)

print("Hospital Billing System")
print("-------------------------------")

print(patient1.get_name())
patient1.display_patient_type()
patient1.calculate_bill()
print("\n", end="")

print(patient2.get_name())
patient2.display_patient_type()
patient2.calculate_bill()
print("\n", end="")

print(patient3.get_name())
patient3.display_patient_type()
patient3.calculate_bill()
