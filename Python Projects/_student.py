class Student:
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores

    def get_score(self):
        return sum(self.scores) / len(self.scores)

    def __str__(self):
        return f"{self.name}[{self.age}]"

# do not modify the below code
student = Student('Alex', 18, [45, 46, 50, 49, 45])
print(f'CGPA of {student} is {student.get_score()}')
