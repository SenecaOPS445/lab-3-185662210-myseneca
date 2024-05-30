#!/usr/bin/env python3

#Author: Ched Duloy
#Author ID: 185662210
#Date Created: 2024/05/30

#return_text_value() function
def return_text_value():
    name = 'Terry'
    greeting = 'Good Morning ' + name 
    return greeting

text = return_text_value()
print(text)

#return_number_value() function
def return_number_value():
    num1 = 10
    num2 = 5
    num3 = num1 + num2
    return num3

number = return_number_value()
print('my number is ', number)
print('my number is ' + str(number))
print('my number is ' + str(return_number_value()))

#Main Program

if __name__ == '__main__':
    print('python code')
    import lab3a
    text = lab3a.return_text_value()
    print(text)
    print(lab3a.return_number_value())
