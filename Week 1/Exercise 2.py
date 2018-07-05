#Author: Daniel Zuñiga @ UN, Bogotá (05.07.18)

#Module for manipulating .csv files
import csv

#Auxiliar variables
how_many = -1
total_weight = 0
total_height = 0

#Open and read the content
with open('filaname.csv') as file:
    reader = csv.reader(file)
    #For every row, sum the third ([2]) and fourth element ([3])
    #   ignoring the first row.
    for row in reader:
        how_many += 1
        if not(row[3] == "Weight"):
            total_weight += float(row[3])
        if not(row[2] == "Height"):
            total_height += float(row[2])

#Print result
print("Average:", total_weight / total_height)
