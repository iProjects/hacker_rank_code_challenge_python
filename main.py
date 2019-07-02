# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 08:28:59 2019

@author: USER
"""
import string
    
def solveMeFirst(a,b):
	# Hint: Type return a+b below
    return a + b

def solveMeFirst_function():
    print("enter two number to perform addition....")
    num1 = int(input())
    num2 = int(input())
    res = solveMeFirst(num1,num2)
    print(str(num1) + " plus " + str(num2) + " equals ", end="")
    print(res)

def read_input_and_write_output():
    print("enter a string literal to see its output....")
    inputString = input() # get a line of input from stdin and save it to our variable
    
    # Your first line of output goes here
    print('Hello, World.')
    
    # Write the second line of output
    print("you entered [ " + inputString + " ]")

def data_types_function():    
    i = 4
    d = 4.0
    s = 'HackerRank '
    # Declare second integer, double, and String variables.
    int1 =  0
    sum_int =  0
    double1 =  0.0
    sum_double =  0.0
    string1 =  ""
    # Read and save an integer, double, and String to your variables.
    print("enter one integer to perform addition with " + str(i) + "....")
    int1 =  int(input())
    print("enter one double to perform addition with " + str(d) + "....")
    double1 =  float(input())
    print("enter string to perform concatenation....")
    string1 =  input()
    # Print the sum of both integer variables on a new line.
    sum_int = i + int1
    print(str(i) + " plus " + str(int1) + " equals " + str(sum_int))
    # Print the sum of the double variables on a new line.
    sum_double = d + double1
    print(str(d) + " plus " + str(double1) + " equals " + str(sum_double))
    # Concatenate and print the String variables on a new line
    # The 's' variable above should be printed first.
    print(s + string1)

def sum_arrays_fucntion():
    print('')


print('hacker rank in python <<<<<<<<<<!!!!!!!!!!!!>>>>>>>>>>>')
solveMeFirst_function()
read_input_and_write_output()
data_types_function()
sum_arrays_fucntion()
    





