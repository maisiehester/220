"""
Maisie Hester
lab2.py
Problem: Arithmetic Functions


"""
import math

def sum_of_three():
    upper_bound = eval(input( " Enter upper bound: "))
    acc = 0
    for i in range( 0, upper_bound, 3):
        acc = i + acc
    print(acc)

def multiplication_table():
    for H in range(1,11):
        for L in range(1,11):
            print(H * L, end=" ")
        print()



def triangle_area():
    A = eval(input( " Enter side a: "))
    B = eval(input( " Enter side b: "))
    C = eval(input( " Enter side c: "))
    S = ( A + B + C ) / 2
    a = math.sqrt(S*(S-A)*(S-B)*(S-C))
    print(a)

def sumSquare():
    lower_bound = eval(input( " Enter lower bound: "))
    upper_bound = eval(input( " Enter upper bound: "))
    acc = 0
    for x in range(lower_bound, upper_bound + 1):
        acc = acc + (x**2)
    print(acc)

def power():
    base = eval(input("Enter base: "))
    exponent = eval(input("Enter exponent: "))
    acc = 1
    for i in range(exponent):
        acc = acc * base
    print(acc)
