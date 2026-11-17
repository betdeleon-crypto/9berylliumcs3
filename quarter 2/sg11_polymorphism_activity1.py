class Patient:    #initiates parent class patient
  def __init__(self, name : str, bill_amount : float):    #defines all attributes
    #makes all attributes into private
    self.__name = name
    self.__bill_amount = bill_amount

  def get_name(self):    #defines method to get name
    return self.__name

  def set_name(self,name):    #defines method to set name
    self.__name = str(name)

  def get_bill_amount(self):  #defines method to get the bill amount
    return self.__bill_amount

  def set_bill_amount(self,bill_amount):    #defines method to set bill amount
    self.__bill_amount = float(bill_amount)

  def calculate_bill(self):        #displays calculated bill amount with no discount
    print("Original Bill:", "₱", self.get_bill_amount())
    print("Final Bill:", "₱", self.get_bill_amount())

  def display_patient_type(self):    #displays patient type as regular patient
    print("Regular Patient")

class Senior(Patient):
  def __init__(self,name : str, bill_amount : float):    #defines all inherited attributes
    super().__init__(name, bill_amount)

  def calculate_bill(self):        #displays calculated bill amount with 20% discount
          #20% discount
    print("Original Bill:", "₱", self.get_bill_amount())    #prints initial bill
    discount = self.get_bill_amount() * 0.20      #calculates discount
    total_bill = self.get_bill_amount() - discount      #calculates final bill with discount
    self.set_bill_amount(total_bill)      #sets the final bill
    print("Final Bill:", "₱", self.get_bill_amount())   #displays final bill

  def display_patient_type(self):    #displays patient type as senior citizen patient
    print("Senior Citizen")

class PhilHealth(Patient):
  def __init__(self, name : str, bill_amount : float):    #defines all inherited attributes
    super().__init__(name, bill_amount)
    
  def calculate_bill(self):        #displays calculated bill amount with 15% discount
      #15% discount
    print("Original Bill:", "₱", self.get_bill_amount())    #prints initial bill
    discount = self.get_bill_amount() * 0.15      #calculates discount
    total_bill = self.get_bill_amount() - discount    #calculates final bill with discount
    self.set_bill_amount(total_bill)      #sets the final bill
    print("Final Bill:", "₱", self.get_bill_amount())  #displays final bill

  def display_patient_type(self):    #displays patient type as philhealth member patient
    print("PhilHealth Member")

#makes all objects from each class
patient1 = Patient("Juan Dela Cruz", 15000)
patient2 = Senior("Maria Santos", 15000)
patient3 = PhilHealth("Pedro Reyes", 15000)

#starts output
print("Hospital Billing System")
print("-------------------------------")

print(patient1.get_name())        #displays patient name
patient1.display_patient_type()   #displays patient type
patient1.calculate_bill()         #displays patient's bill
print("\n", end="")               #prints an empty line

print(patient2.get_name())        #displays patient name
patient2.display_patient_type()   #displays patient type
patient2.calculate_bill()         #displays patient's bill
print("\n", end="")               #prints an empty line

print(patient3.get_name())        #displays patient name
patient3.display_patient_type()   #displays patient type
patient3.calculate_bill()         #displays patient's bill
