#Author: Daniel Zuñiga @ UN, Bogotá (05.07.18)

#Auxiliar variable
age = ""

#Ask the user to enter his/her age. Will ask again if answer isn't a number.
while not(age.isdigit()):
    age = input("Your age please: ")

#Having a number as answer, proceeds to cast the string into an integer.
age = int(age)

#Verifies age and if the user should or not be at school.
if (age >= 14 and age <=18):
    print("Yo, you should be at school")
else:
    print("Not at school but hope you're learning something")
