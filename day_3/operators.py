>>> age = 22
>>> height = 6.0
>>> complex_number = 3+4j
>>> base = float(input("Enter base: "))
Enter base: 20
>>> height = float(input("Enter height: "))
Enter height: 10
>>> area = 0.5*base*height
>>> print("The area of the triangle is: ", area)
The area of the triangle is:  100.0
>>> length = int(input("Enter length: "))
Enter length: 3
>>> width = int(input("Enter width: "))
Enter width: 4
>>> area = length*width
>>> perimeter = 2*(length+width)
>>> print("Area: ", area)
Area:  12
>>> print("Perimeter: ",perimeter)
Perimeter:  14
>>> slope = 2
>>> y_intercept = -2
>>> x_intercept = (0-y_intercept)/slope
>>> print("Slope: ",slope)
Slope:  2
>>> print("x-intercept: ",x_intercept)
x-intercept:  1.0
>>> print("y-intercept: ",y_intercept)
y-intercept:  -2
>>> print(len('python') != len('dragon'))
False
>>> print('on' in 'python' and 'dragon')
dragon
>>> print('on' in 'python')
True
>>> print('on' in 'dragon')
True
>>> print('on' not in 'dragon' and 'on' not in 'python')
False
>>> len_python = len('python')
>>> print(len_python)
6
>>> print(float(len_python))
6.0
>>> print(str(len_python))
6
>>> number = int(input("Enter a number: "))
Enter a number: 8
>>> if number % 2 ==0:
... print("The number is even")
  File "<stdin>", line 2
    print("The number is even")
    ^^^^^
IndentationError: expected an indented block after 'if' statement on line 1
>>> if number % 2 == 0:
...     print("The number is even")
... else:
...     print("The number is odd")
...
The number is even
>>> number
8
>>> print(type('10') == type(10))
False
>>> print(int('9.8') == 10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '9.8'
>>> print(int(float('9.8')) == 10)
False
>>> hours = int(input("Enter hours: ")
...
... )
Enter hours: 40
>>> rate_per_hour = int(input("Enter rate per hour: ")
... )
Enter rate per hour: 28
>>> weekly_earning = hours*rate_per_hour
>>> print("Your weekly earning is ", weekly_earning)
Your weekly earning is  1120
>>> for i in range (1,6):
...     print(i, 1, i, i**2, i**3)
...
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
