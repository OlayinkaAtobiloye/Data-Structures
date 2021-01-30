class Student:
    def __init__(self, age, weight, height):
        """a constructor that takes in 3 parameters, a students age,weight and height(in that order)
    and initializes them to those values"""
        self.age = age
        self.weight = weight
        self.height = height

    def info(self):
        """returns a tuple containing the age and Body Mass Index(BMI)(rounded to 2dp) of the student
    BMI=weight/(height**2)"""
        self.BMI = self.weight / (self.height ** 2)
        return self.age, round(self.BMI, 2)


def average(StudentList):
    """takes a list of student objects and RETURNS a tuple containing the average age,weight and height(in that order)
    of the students in the next 10 years
    i.e 10 years from now what would be their average age,weight and height(in that order)
    Assume that weight increases by 5% each year and height increases by 2% each year."""
    totalAge = 0
    totalWeight = 0
    totalHeight = 0
    for student in StudentList:
        years = 0
        age, weight, height = student.age, student.weight, student.height
        while years < 10:
            age += 1
            height += (2 * height) / 100
            weight += (5 * weight) / 100
            years += 1
        totalAge += age
        totalHeight += height
        totalWeight += weight
    return (totalAge/2), round((totalWeight/2), 2), round((totalHeight/2), 2)


Joba = Student(22, 40.01, 8.3)
Fortune = Student(23, 45.67, 7.6)
print(Fortune.info())
print(average([Joba, Fortune]))
print(Fortune.age)
print(Fortune.BMI)

a = 'boy'
print (a)