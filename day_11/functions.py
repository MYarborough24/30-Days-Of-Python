>>> def add_two_numbers ():
...     )
  File "<stdin>", line 2
    )
    ^
SyntaxError: unmatched ')'
>>> def add_two_numbers (num_one, num_two):
...     sum = num_one + num_two
...     return sum
...
>>> print(add_two_numbers(1,9))
10
>>> def area_of_circle (r):
...     pi = 3.14
...     area = pi * r ** 2
...     return area
...
>>> print(area_of_circle(10))
314.0
>>> def convert_celsius_to_fahrenheit (c):
...     f = (c*9/5) + 32
...     return f
...
>>> print(convert_celsius_to_fahrenheit(25))
77.0
>>> def print_list(items):
...     for item in items:
...             print(item)
...
>>> fruits = ['banana', 'mango', 'apple', 'kiwi']
>>> print_list(fruits)
banana
mango
apple
kiwi
>>> def reverse_list(lst):
...     reverse_list = []
...     for i in range(len(reverse_list) -1, -1, -1):
...             reverse_list.append(i)
...     return reverse_list)
  File "<stdin>", line 5
    return reverse_list)
                       ^
SyntaxError: unmatched ')'
>>> def reverse_list(lst):
...     reversed_list = []
...
>>>     for i in range(len(lst) - 1, -1, -1):
  File "<stdin>", line 1
    for i in range(len(lst) - 1, -1, -1):
IndentationError: unexpected indent
>>>         reversed_list.append(lst[i])
  File "<stdin>", line 1
    reversed_list.append(lst[i])
IndentationError: unexpected indent
>>>
>>> def reverse_list(lst):
...     reversed_list = []
...     for i in range(len(lst) -1, -1, -1):
...             reversed_list.append(lst[i])
...     return reversed_list
...
>>> print(reverse_list([1,2,3,4,5]))
[5, 4, 3, 2, 1]
>>> def sum_of_numbers(n):
...     total = 0
...     for i in range(1, n+1):
...             total += n
...     return total
...
>>> print(sum_of_numbers(5))
25
>>> def sum_of_numbers(n):
...     total = 0
...     for i in range(1, n+1):
...             total += i
...     return total
...
>>> print(sum_of_numbers(5))
15
