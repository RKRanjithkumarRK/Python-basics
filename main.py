""""print("The filght attendant asked, \"May I see your boarding pass?\" ")
print('Hello', end=' ')
print('World',end=' ')
print('Good  Bye',end=' ')

Num1 = int(input())
print("Enter the number: ", Num1)
print(type(Num1))

Length = int(input())
Breadth = int(input())
Area = Length * Breadth
print("Area of rectangle: ", Area)

num1 = int(input())
num2 = float(input())

Sum = num1 + num2
print(Sum)

Name = input("Enter the name: ")
Age = eval(input("Enter age: "))
Gender = input("Enter gender: ")
Height = eval(input("Enter the height: "))
print("Name: ", Name)
print("Age: ", Age)
print("Gender: ", Gender)
print("Height: ", Height)

radius = int(input("Enter the radius of a circle: "))
print("Radius = ", radius)
PI = 3.1428
Area = PI * radius * radius
print("Area of a circle is : ", Areaa)


import math
Base = int(input("Enter the base of the right angled triangle: "))
Height = int(input("Enter the height of the right angled triangle: "))
print("Enter the details are as follows: ")
print("BASE =", Base)
print("HEIGHT =", Height)
Hypotenuse = math.sqrt(Base * Base + Height * Height)
print("HYPOTENUSE = ", Hypotenuse)

char1 = 'b'
char2 = 'B'
print('Letter\tASCII Value')
print(char1, '\t', ord(char1))
print(char2, '\t', ord(char2))
print('Difference between ASCII value of two Letters: ')
print(ord(char1), '-', ord(char2), '=', end=' ')
print(ord(char1)-ord(char2))

w1 = eval(input('Enter the weight of the object in grams: '))
print('Weight of object = ', w1, 'grams')
w2 = w1 // 1000
w3 = w1 % 1000
print('Weight of object = ', w2, 'kg and ', w3, 'g')

num = eval(input('Enter four-digit number: '))
print('Entered number is: ', num)
r1 = num%10
q1 = num//10
r2 = q1%10
q2 = q1//10
r3 = q2%10
q3 = q2//10
r4 = q3%10
print('Reverse of ', num, 'is: ', r1, r2, r3, r4)"


length = eval(input("Enter the length of the rectangle: "))
breadth = eval(input("Enter the breadth of the rectangle: "))
print("Length = ", length)
print("Breadth = ", breadth)
perimeter = 2 * (length + breadth)
print(perimeter)

p = 4
q = 2
z = (2 + 8 * p) // 2 - ((p - q) * (p + q)) // 2 + 4 * ((p+q) // 2)
print('Where p = ', p, 'and Q = ', q)
print('Answer for above expression = ', z)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(num1,' & ',num2,' = ',num1 & num2)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(num1,' | ',num2,' = ',num1 | num2)

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
print(num1,' ^ ',num2,' = ',num1 ^ num2)

N = int(input('Enter number: '))
S = int(input('Enter number of bits to be shift right: '))
print(N,' >> ',S,' = ',N >> S)

N = int(input('Enter number: '))
S = int(input('Enter number of bits to be shift Left: '))
print(N,' << ',S,' = ',N << S)

radius = eval(input('Enter the radius of a circle: '))
print('Radius = ', radius)
radius **= 2
area = 3.14
area *= radius
print('Radius of a circle = ', area)

CP = int(input('Enter the Cost of product: '))
CGST = float(input('Enter the amount % imposed by Central, i.e , CGST: '))
SGST = float(input('Enter the amount % imposed by State, i.e , SGST: '))
Amount_Cgst = (CGST/100 * CP)
Amount_Sgst = (SGST/100 * CP)
Total = CP + Amount_Cgst + Amount_Sgst
print('Total cost of the product: ', Total)

X = 5
Y = 5
print(X/Y)

N = int(input('Enter number: '))
S = int(input('Enter number of bits to be shift Left: '))
print(N,' << ',S,' = ',N << S)

length =  eval(input('Enter the length of a rectangle: '))
breadth = eval(input('Enter the breadth of a rectangle: '))
print('Length = ', length)
print('Breadth = ', breadth)
area = length * breadth
print('The area of a rectangle = ',area)

p, q, r = eval(input('Enter Three numbers: '))
print('P = ', p, 'q = ', q, 'r = ', r)
print('(p > q > r) is ', p > q > r)
print('(p < q < r) is ', p < q < r)
print('(p < q) and (q < z) are ', (p< q) and (q < r))
print('(p < q) or (q < r) is ', (p < q) or (q < r))

num1 = eval(input('Enter the number: '))
num2 = eval(input('Enter the number: '))
if num1-num2 == 0:
    print('Both the numbers are equal')

Number = eval(input('Enter the number: '))
if Number>0:
    Number = Number * Number
print(Number)

from math import pi
Radius = eval(input('Enter the radius of a circle: '))
if Radius>0:
    Area = Radius * Radius * pi
    print('Area of a circle is: ', format(Area, ".2f"))
    circumference = 2 * pi * Radius
    print('circumference of a circle is: ', format(circumference, ".2f"))

num1 = int(input('Enter the number: '))
num2 = int(input('Enter the number: '))
if num1 > num2:
    print(num1, 'is greater than', num2)
else:
    print(num2, 'is greater than', num1)

Sales =  float(input('Enter the total Gross salary: '))
if Sales >= 100000:
    basic = 4000
    hra = 20 * basic/100
    da = 110 * basic/100
    conveyance = 500
    incentive = Sales * 10/100
    bonus = 1000
else:
    basic = 4000
    hra = 10 * basic/100
    da = 110 * basic/100
    conveyance = 500
    incentive = Sales * 4/100
    bonus = 500

salary = basic + hra + da + conveyance + incentive + bonus
print('Basic = ', basic)
print('Hra = ', hra)
print('Da = ', da)
print('Conveyance = ', conveyance)
print('Incentive = ', incentive)
print('Bonus = ', bonus)
print('The total gross salary is: ', salary)

num = int(input('Enter the number: '))
print('Entered number is: ',  num)
if num % 5==0 and num % 10==0:
    print(num, 'is divisible by both 5 and 10')
if num % 5==0 or num % 10==0:
    print(num, 'is divisible by 5 or 10')
else:
    print(num, 'is not divisible either by 5 or 10')

num1 = int(input('Enter the number: '))
num2 = int(input('Enter the number: '))
num3 = int(input('Enter the number: '))
if num1 > num2:
    if num2 > num3:
        print(num1, 'is greater than', num2, 'and', num3)
else:
    print(num1, 'is less than', num2, 'and', num3)

sub1 = int(input('Enter the mark of data structure: '))
sub2 = int(input('Enter the mark of python: '))
sub3 = int(input('Enter the mark of machine learning: '))
sub4 = int(input('Enter the mark of deep learning: '))
sub5 = int(input('Enter the mark of Gen AI: '))

sum = sub1 + sub2 + sub3 + sub4 + sub5
per = sum/5
print('Total marks of Student is ', sum, 'in all subjects')
print('Percentage', per)

if per>=90:
    print('Distinction')
else:
    if per>=80:
        print('First class')
    else:
        if per>=70:
            print('Second class')
        else:
            if per>=60:
                print('Pass')
            else:
                print('Fail')

day = int(input('Enter the day of the week: '))
if day == 1:
    print('It is monday')
elif day == 2:
    print('It is Tuesday')
elif day == 3:
    print('It is Wednesday')
elif day == 4:
    print('It is Thursday')
elif day == 5:
    print('It is Friday')
elif day == 6:
    print('It is saturday')
elif day == 7:
    print('It is sunday')
else:
    print('Sorry the week contains only 7 days')"""
from random import choice

num1 = float(input('Enter the number: '))
num2 = float(input('Enter the number: '))
print('1) Addition')
print('2) Subtraction')
print('3) Multiplication')
print('4) Division')

if choice == 1:
    print()