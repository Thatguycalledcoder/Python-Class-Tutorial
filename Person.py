class Person:
    def __init__(self,initialAge):
        #Checks if age is less than 0 then sets to 0 if so
        if (initialAge < 0):
            self.age = 0
            print("Age is not valid, setting age to 0.")
        else:
            self.age = initialAge
    #Checks the status of a person according to age range
    def amIOld(self):
        if (self.age < 13):
            print("You are young.")
        elif ((self.age >= 13) and (self.age < 18)):
            print("You are a teenager.")
        else:
            print("You are old.")
    #This function increments the age by one. Simulates a year gone by
    def yearPasses(self):
        self.age += 1

#Simple instantiation of Person object
peter = Person(9)
peter.amIOld()
peter.yearPasses()
