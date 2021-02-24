#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:carrot
# Time :2020/9/26 23:13

class Student:
    def __init__(self):#两者之间的区别
        self.name = None
        self.score = None

    # def __init__(self, name, score):
    #     self.name = name
    #     self.score = score

    def print_score(self):
        print("%s score is %s" % (self.name, self.score))

    def get_grade(self):
        if self.score >= 80:
            return "A"
        elif self.score >= 70:
            return "B"
        else:
            return "C"

#student = Student("sansan", 90)
student = Student()
student.name= "sansan"
student.score = 90

# susan = Student("sunny", 78)
susan = Student()
susan.name = "susan"
susan.score = 8

student.print_score()
susan.print_score()
print('******')
print(susan.get_grade())
print(student.get_grade())