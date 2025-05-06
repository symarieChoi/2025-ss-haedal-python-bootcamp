class Student:
    # 생성자(초기화 메소드)
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    # 학점을 반환하는 메소드
    def get_grade(self):
        if self.grade >= 90:
            return 'A'
        elif self.grade >= 80:
            return 'B'
        elif self.grade >= 70:
            return 'C'
        else:
            return 'F'

i = int(input("학생 수를 입력하시오: "))
s = []

for _ in range(i):
    name, grade = input().split()
    grade = int(grade)
    student = Student(name, grade)
    s.append(student)

for student in s:
    print(f"{student.name} {student.get_grade()}")