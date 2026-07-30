>>> empty_list = list()
>>> numbers = [0,1,2,3,4,5]
>>> print(len(numbers))
6
>>> first_item = numbers[0]
>>> middle_item = numbers[len(numbers)//2]
>>> last_item = numbers[-1]
>>> mixed_data_types = ['Matt', 22, '6'0"', 'Single', '510 Fairfield Way SW, Leesburg, VA 20175']
  File "<stdin>", line 1
    mixed_data_types = ['Matt', 22, '6'0"', 'Single', '510 Fairfield Way SW, Leesburg, VA 20175']
                                        ^
SyntaxError: unterminated string literal (detected at line 1)
>>> it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
>>> print(it_companies)
['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
>>> first=it_companies[0]
>>> middle=it_companies[len(it_companies)//2]
>>> last=it_companies[-1]
>>> print(first,middle,last)
Facebook Apple Amazon
>>> print(len(it_companies))
7
>>> it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
>>> first=it_companies[0]
>>> >>> middle=it_companies[len(it_companies)//2]
  File "<stdin>", line 1
    >>> middle=it_companies[len(it_companies)//2]
    ^^
SyntaxError: invalid syntax
>>> middle=it_companies[len(it_companies)//2]
>>> last=it_companies[-1]
>>> it_companies[4]="Tesla"
>>> print(it_companies)
['Facebook', 'Google', 'Microsoft', 'Apple', 'Tesla', 'Oracle', 'Amazon']
>>> middle_index = len(companies)//2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'companies' is not defined. Did you mean: 'it_companies'?
>>> middle_index = len(it_companies)//2
>>> it_companies.insert(middle_index,'Intel')
>>> it_companies[1].upper()
'GOOGLE'
>>> print(it_companies)
['Facebook', 'Google', 'Microsoft', 'Intel', 'Apple', 'Tesla', 'Oracle', 'Amazon']
>>> it_companies[1]=it_companies[1].upper()
>>> print(it_companies)
['Facebook', 'GOOGLE', 'Microsoft', 'Intel', 'Apple', 'Tesla', 'Oracle', 'Amazon']
>>> result = "#; ".join(it_companies)
>>> print(result)
Facebook#; GOOGLE#; Microsoft#; Intel#; Apple#; Tesla#; Oracle#; Amazon
>>> it_companies.sort()
>>> print(it_companies.sort())
None
>>> print(it_companies)
['Amazon', 'Apple', 'Facebook', 'GOOGLE', 'Intel', 'Microsoft', 'Oracle', 'Tesla']
>>> it_companies.sort(reverse=True)
>>> print(it_companies)
['Tesla', 'Oracle', 'Microsoft', 'Intel', 'GOOGLE', 'Facebook', 'Apple', 'Amazon']
>>> does_exist = 'Microsoft' in it_companies
>>> print(does_exist)
True
>>> first_three=it_companies[0:3]
>>> print(first_three)
['Tesla', 'Oracle', 'Microsoft']
>>> middle=it_companies[len(it_companies)//2]
>>> print(middle)
GOOGLE
>>> it_companies.remove(middle)
>>> print(it_companies)
['Tesla', 'Oracle', 'Microsoft', 'Intel', 'Facebook', 'Apple', 'Amazon']
>>> del it_companies
>>> print(it_companies)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'it_companies' is not defined
>>> front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
>>> back_end = ['Node','Express', 'MongoDB']
>>> front_end.extend(back_end)
>>> print(front_end)
['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
