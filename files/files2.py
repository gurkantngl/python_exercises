# -*- coding: utf-8 -*-

students = ["Engin", "Derin", "Salih", "Ali", "Ayşe"]

fileToAppend = open("ogrenciler.txt","a")

for student in students:
    fileToAppend.write(student)
    fileToAppend.write("\n")

fileToAppend.close()