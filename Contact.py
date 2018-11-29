#Yining Hua
#CSC220
#January 30,2018
#Objective: write a Contact class that stores the following: name,
#phone number, email address and checks to make sure that the phone
#number and email address are valid

def main():
	ewon = Contact("Ewon","","ewonsmith.edu")
	ewon.check_phone()
	ewon.check_email()
	print(ewon.name)
	print(ewon.phone)
	print(ewon.email)
	

class Contact():
	def __init__(self,name,phone,email):
		self.name = name
		self.phone = phone
		self.email = email

	def check_phone(self):
		if not self.phone:
			self.phone= "Unknown"
		elif len(self.phone)!=10:
			self.phone = "Not a valid US number."

	def check_email(self):
		if not self.email:
			self.email= "Unkown"
		elif not ("@" in self.email):
			self.email = "Not a valid email address."

main()

