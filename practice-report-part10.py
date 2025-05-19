#10.1

#(1) 123 + 334
(123).__add__(334)
print(123+334)

#(2) 123 - 334
(123).__sub__(334)
print(123 - 334)

#(3) 123 * 334
(123).__mul__(334)
print(123 * 334)

#(4) 123/3
(123).__truediv__(3)
print(123/3)

#10.3

# pop() 사용 불가능
# sort() 사용 불가능
# append() 사용 불가능
# upper() 사용 가능
# insert() 사용 불가능
# remove() 사용 불가능

#10.5
#10.7

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return "이름은{self.name}이고, 나이는 {self.age}살입니다."

my_dog=Dog('mango',3)
print(my_dog)

#10.9

class Counter:
    def __init__(self, number = 0):
        self.number=number
        if self.number>= 100:
            self.number=0
        elif self.number <=-1:
            self.number = 0
    def reset(self):
        self.number = 0
        def inc(self):
            self.number = self.number + 1
            if self.number>= 100:
                self.number = 0
    def dec(self):
        self.number = self.number - 1
        if self.number <=-1:
            self.number = 0
    def __str__(self):
        return "C((self.number))"
    def __add__(self, other):
        return Counter(self.number + other.number)
    def __sub__(self, other):
        return Counter(self.number - other.number)
c1 = Counter(10)
c2 = Counter(20)
c3 = c1 + c2
c4 = c1 - c2
print(f"c3 = {c3}")
print(f"c4 = {c4}")

#10.11

class Student:
    def __init__(self, name, student_id, korean_quiz=0, math_quiz=0, science_quiz=0):
        self.name = name
        self.student_id = student_id
        self.korean_quiz = korean_quiz
        self.math_quiz = math_quiz
        self.science_quiz = science_quiz

    def __str__(self):
        return '이름 : {}, 학번 : {} \n국어성적 : {}, 수학성적 : {}, 과학성적 : {} \n' \
            '합계 : {}, 평균 : {}'.format(self.name, self.student_id, self.korean_quiz, \
                self.math_quiz, self.science_quiz, self.get_total_score(), \
                    self.get_avg_score())
    def get_name(self):
        return self.name
    def get_student_id(self):
        return self.student_id
    def get_korean_quiz(self):
        return self.korean_quiz
    def get_math_quiz(self):
        return self.math_quiz
    def get_science_quiz(self):
        return self.science_quiz
    def set_korean_quiz(self, korean_quiz):
        self.korean_quiz = korean_quiz
    def set_math_quiz(self, math_quiz):
        self.math_quiz = math_quiz
    def set_science_quiz(self, science_quiz):
        self.science_quiz = science_quiz
    def get_total_score(self):
        return self.korean_quiz + self.math_quiz + self.science_quiz
    def get_avg_score(self):
        return self.get_total_score() / 3.0

name = input('학생의 이름을 입력하세요 : ')
student_id = input('학생의 학번을 입력하세요 : ')
student = Student(name, student_id)
korean_quiz = int(input('학생의 국어 성적을 입력하세요 : '))

math_quiz = int(input('학생의 수학 성적을 입력하세요 : '))
science_quiz = int(input('학생의 과학 성적을 입력하세요 : '))
student.set_korean_quiz(korean_quiz)
student.set_math_quiz(math_quiz)
student.set_science_quiz(science_quiz)
print(student)

#10.13

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def __str__(self):
        return f"Rectangle : (x = {self.x}, y = {self.y}, w = {self.width}, h = {self.height})"
    def overlaps(self, r):
        return not (self.x + self.width < r.x or r.x + r.width < self.x or self.y - self.height > r.y or r.y - r.height > self.y)
    def contains(self, r):
        return (self.x <= r.x and self.x + self.width >= r.x + r.width and self.y >= r.y and self.y - self.height <= r.y - r.height)
r1 = Rectangle(0, 0, 100, 100)
r2 = Rectangle(0, -10, 10, 10)
r3 = Rectangle(-100, 0, 120, 100)
print('r1 =', r1)
print('r2 =', r2)
print('r3 =', r3)
print('r1 contains r2 :', r1.contains(r2))
print('r1 contains r3 :', r1.contains(r3))
print('r1 overlaps r2 :', r1.overlaps(r2))
print('r1 overlaps r3 :', r1.overlaps(r3))

