# gpa.py
#   Program to find student with highest GPA

# Creating class containing student information
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

    # Calculates the student's GPA
    def gpa(self):
        return self.qpoints / self.hours

def make_student(infoStr):
    # infoStr is a tab-separated line: name hours qpoints
    # returns a corresponding Student object
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)

# Calling main function
def main():
    # Testing out making an object
    # Creating student object
    student_1 = Student("Adams Henry", 127, 228)

    #Printing the student's name
    print(student_1.get_name())

    # Open the input file of rreading
    filename = input("Enter the name of the grade file: ")
    infile = open(filename, "r")

    # Set best to the record for the first student in the file
    best = make_student(infile.readline())

    # Process subsequent lines of the file
    for line in infile:
        # Turn the line into a student record
        s = make_student(line)
        # If this student is best so far, remember it
        if s.gpa() > best.gpa():
            best = s 


if __name__ == '__main__':
    main()
