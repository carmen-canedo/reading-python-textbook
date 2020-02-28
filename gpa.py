# gpa.property
#   Calculating the gpa of a student

class Student:

    # Initializing instance variables
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    # Writing methods
    ## Gets name of object
    def get_name(self):
        return self.name

    ## Gets hours taken by student
    def get_hours(self):
        return self.hours

    # Gets the quality points of the student
    def get_qpoints(self):
        return self.qpoints

# Calling main function
def main():

    # Creating student object
    student_1 = Student("Adams Henry", 127, 228)

    #Printing the student's name
    print(student_1.get_name())



if __name__ == '__main__':
    main()
