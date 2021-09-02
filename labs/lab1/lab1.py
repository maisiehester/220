"""
<Maisie Hester>
lab1.py
Problem: This function calculates the area of a rectangle
"""



def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)

def shooters_percentage():
    totalShots = eval(input("Enter the total shots: "))
    shotsMade = eval(input("Enter the shots made: "))
    shootersPercentage = shotsMade / totalShots * 100
    print("percentage =", shootersPercentage)

def coffee():
    pounds = eval(input("Enter the total pounds: "))
    cost = 10.5 * pounds + .86 * pounds + 1.50
    print("cost", cost)

def kilometers_to_miles():
    totalKilometers = eval(input("Enter the total kilometers: "))
    miles = totalKilometers / 1.61
    print("miles", miles)

def calc_area():
    length = 20
    width = 5
    area = length * width
    print("Area =", area)





