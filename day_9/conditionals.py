>>> age = int(input('Enter your age: '))
Enter your age: 30
>>> if age >= 18:
...     print('You are old enough to drive.')
... else:
...     years_left = 18 - age
...     print(f'You need {years_left} more years to learn to drive.')
...
You are old enough to drive.
>>> 15
15
>>> print(age)
30
>>> age = 15
>>> num1 = int(input('Enter number one: '))
Enter number one: 4
>>> num2 = int(input('Enter number two: '))
Enter number two: 3
>>> if num1 > num2:
...     print(f'{num1} is greater than {num2}')
... elif num1 < num2:
...     print(f'{num1} is smaller than {num2}')
... else:
...     print(f'{num1} is equal to {num2}')
...
4 is greater than 3
>>> score = int(input('Enter your test score: '))
Enter your test score: 86
>>> if 90 <= score <= 100:
...     print('Grade: A')
... elif 80 <= score <= 89:
...     print('Grade: B')
... elif 0 <= score <= 79:
...     print('Grade: C, D, or F')
... else:
...     print('Invalid score')
...
Grade: B
>>>         person={
  File "<stdin>", line 1
    person={
IndentationError: unexpected indent
>>>     'first_name': 'Asabeneh',
  File "<stdin>", line 1
    'first_name': 'Asabeneh',
IndentationError: unexpected indent
>>>     'last_name': 'Yetayeh',
  File "<stdin>", line 1
    'last_name': 'Yetayeh',
IndentationError: unexpected indent
>>>     'age': 250,
  File "<stdin>", line 1
    'age': 250,
IndentationError: unexpected indent
>>>     'country': 'Finland',
  File "<stdin>", line 1
    'country': 'Finland',
IndentationError: unexpected indent
>>>     'is_married': True,
  File "<stdin>", line 1
    'is_married': True,
IndentationError: unexpected indent
>>>     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
  File "<stdin>", line 1
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
IndentationError: unexpected indent
>>>     'address': {
  File "<stdin>", line 1
    'address': {
IndentationError: unexpected indent
>>>         'street': 'Space street',
  File "<stdin>", line 1
    'street': 'Space street',
IndentationError: unexpected indent
>>>         'zipcode': '02210'
  File "<stdin>", line 1
    'zipcode': '02210'
IndentationError: unexpected indent
>>>     }
  File "<stdin>", line 1
    }
IndentationError: unexpected indent
>>> person={
... 'first_name': 'Asabeneh',
...     'last_name': 'Yetayeh',
...     'age': 250,
...     'country': 'Finland',
...     'is_married': True,
...     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
...     'address': {
...         'street': 'Space street',
...
...
... }
... }
>>> person = {
...     'first_name': 'Asabeneh',
...     'last_name': 'Yetayeh',
...     'age': 250,
...     'country': 'Finland',
...     'is_married': True,
...     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
...     'address': {
...         'street': 'Space street',
...         'zipcode': '02210'
...     }
... }
>>> if 'skills' in person:
...     skills = person['skills']
...     middle_skill = [len(skills) // 2]
...     print('Middle skill: ',middle_skill)
...
Middle skill:  [2]
>>> if 'skills' in person:
...     print('Python' in person['skills'])
...
True
>>> if person['is_married'] and person['country'] == 'Finland':
...     print(f'{person['first_name']} {person['last_name']}
  File "<stdin>", line 2
    print(f'{person['first_name']} {person['last_name']}
          ^
SyntaxError: unterminated f-string literal (detected at line 2)
>>> if person['is_married'] and person['country'] == 'Finland':
...     print(
...             f'{person['first_name']} {person['last_name']} lives in '
...             f'{person['country']}. His married.'
...     )
...
Asabeneh Yetayeh lives in Finland. His married.
