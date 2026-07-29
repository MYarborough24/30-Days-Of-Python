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
