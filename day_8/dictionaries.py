>>> dog = {}
>>> dog['name' 'color'] = 'Annie' 'Black'
>>> print(dog)
{'namecolor': 'AnnieBlack'}
>>> del dog
>>> dog = {}
>>> dog['name'] = 'Annie'
>>> dog['color'] = 'Black'
>>> dog['breed'] = 'Black Lab'
>>> dog['legs'] = 4
>>> dog['age'] = 14
>>> student = {
...     'first_name':'Matt'
...     'last_name':'Yarborough'
  File "<stdin>", line 3
    'last_name':'Yarborough'
               ^
SyntaxError: invalid syntax
>>>     'first_name':'Matt',
  File "<stdin>", line 1
    'first_name':'Matt',
IndentationError: unexpected indent
>>> print(student)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'student' is not defined
>>> student = {
...     'first_name':'Matt',
...     'last_name':'Yarborough',
...     'gender':'Male'
...     ,'age':22,
...     'is_married':False,
...     'skill':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
...     'country':'United State',
...     'city':'Leesburg',
...     'address':{
...             'street':'Fairfield Way',
...             'zipcode':'20175'
...     }
...     }
>>> print(len(student))
9
>>> skills = student['skill']
>>> print(skills)
['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
>>> print(type(skills))
<class 'list'>
>>> student['skill'].append('HTML','R')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list.append() takes exactly one argument (2 given)
>>> student['skill'].append('HTML')
>>> print(student)
{'first_name': 'Matt', 'last_name': 'Yarborough', 'gender': 'Male', 'age': 22, 'is_married': False, 'skill': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python', 'HTML'], 'country': 'United State', 'city': 'Leesburg', 'address': {'street': 'Fairfield Way', 'zipcode': '20175'}}
>>> keys = student.keys()
>>> print(keys)
dict_keys(['first_name', 'last_name', 'gender', 'age', 'is_married', 'skill', 'country', 'city', 'address'])
>>> print(student.items())
dict_items([('first_name', 'Matt'), ('last_name', 'Yarborough'), ('gender', 'Male'), ('age', 22), ('is_married', False), ('skill', ['JavaScript', 'React', 'Node', 'MongoDB', 'Python', 'HTML']), ('country', 'United State'), ('city', 'Leesburg'), ('address', {'street': 'Fairfield Way', 'zipcode': '20175'})])
>>> student.pop('skill')
['JavaScript', 'React', 'Node', 'MongoDB', 'Python', 'HTML']
>>> print(student)
{'first_name': 'Matt', 'last_name': 'Yarborough', 'gender': 'Male', 'age': 22, 'is_married': False, 'country': 'United State', 'city': 'Leesburg', 'address': {'street': 'Fairfield Way', 'zipcode': '20175'}}
