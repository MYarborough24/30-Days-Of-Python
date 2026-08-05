>>> for i in range(11):
...     print(i)
...
0
1
2
3
4
5
6
7
8
9
10
>>> while i in range(11):
...
  File "<stdin>", line 2

    ^
IndentationError: expected an indented block after 'while' statement on line 1
>>> i=0
>>> while i<=10:
...     print(i)
...     i+=1
...
0
1
2
3
4
5
6
7
8
9
10
>>> for i in range(1,8):
...     print('#' * i)
...
#
##
###
####
#####
######
#######
>>> for i in range(0,11):
...     print(f"{i} x {i} = {i * i}")
...
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
>>> languages = ['Python', 'Numpy','Pandas','Django', 'Flask']
>>> for i in languages:
...     print(i)
...
Python
Numpy
Pandas
Django
Flask
>>> for i in range(0,100):
...
  File "<stdin>", line 2

    ^
IndentationError: expected an indented block after 'for' statement on line 1
>>> for i in range(0,101):
...     if i % 2 == 0:
...             print(i)
...
0
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
100
>>> total = 0
>>> for i in range(101):
...     total += i
...
>>> print('The sum of all numbers is', total)
The sum of all numbers is 5050
>>> countries = [
...   'Afghanistan',
...   'Albania',
...   'Algeria',
...   'Andorra',
...   'Angola',
...   'Antigua and Barbuda',
...   'Argentina',
...   'Armenia',
...   'Australia',
...   'Austria',
...   'Azerbaijan',
...   'Bahamas',
...   'Bahrain',
...   'Bangladesh',
...   'Barbados',
...   'Belarus',
...   'Belgium',
...   'Belize',
...   'Benin',
...   'Bhutan',
...   'Bolivia',
...   'Bosnia and Herzegovina',
...   'Botswana',
...   'Brazil',
...   'Brunei',
...   'Bulgaria',
...   'Burkina Faso',
...   'Burundi',
...   'Cabo Verde',
...   'Cambodia',
...   'Cameroon',
...   'Canada',
...   'Central African Republic',
...   'Chad',
...   'Chile',
...   'China',
...   'Colombia',
...   'Comoros',
...   'Congo, Democratic Republic of the',
...   'Congo, Republic of the',
...   'Costa Rica',
...   "Côte d'Ivoire",
...   'Croatia',
...   'Cuba',
...   'Cyprus',
...   'Czech Republic',
...   'Denmark',
...   'Djibouti',
...   'Dominica',
...   'Dominican Republic',
...   'East Timor (Timor-Leste)',
...   'Ecuador',
...   'Egypt',
...   'El Salvador',
...   'Equatorial Guinea',
...   'Eritrea',
...   'Estonia',
...   'Eswatini',
...   'Ethiopia',
...   'Fiji',
...   'Finland',
...   'France',
...   'Gabon',
...   'Gambia',
...   'Georgia',
...   'Germany',
...   'Ghana',
...   'Greece',
...   'Grenada',
...   'Guatemala',
...   'Guinea',
...   'Guinea-Bissau',
...   'Guyana',
...   'Haiti',
...   'Honduras',
...   'Hungary',
...   'Iceland',
...   'India',
...   'Indonesia',
...   'Iran',
...   'Iraq',
...   'Ireland',
...   'Israel',
...   'Italy',
...   'Jamaica',
...   'Japan',
...   'Jordan',
...   'Kazakhstan',
...   'Kenya',
...   'Kiribati',
...   'Korea, North',
...   'Korea, South',
...   'Kuwait',
...   'Kyrgyzstan',
...   'Laos',
...   'Latvia',
...   'Lebanon',
...   'Lesotho',
...   'Liberia',
...   'Libya',
...   'Liechtenstein',
...   'Lithuania',
...   'Luxembourg',
...   'Madagascar',
...   'Malawi',
...   'Malaysia',
...   'Maldives',
...   'Mali',
...   'Malta',
...   'Marshall Islands',
...   'Mauritania',
...   'Mauritius',
...   'Mexico',
...   'Micronesia',
...   'Moldova',
...   'Monaco',
...   'Mongolia',
...   'Montenegro',
...   'Morocco',
...   'Mozambique',
...   'Myanmar',
...   'Namibia',
...   'Nauru',
...   'Nepal',
...   'Netherlands',
...   'New Zealand',
...   'Nicaragua',
...   'Niger',
...   'Nigeria',
...   'North Macedonia',
...   'Norway',
...   'Oman',
...   'Pakistan',
...   'Palau',
...   'Palestine',
...   'Panama',
...   'Papua New Guinea',
...   'Paraguay',
...   'Peru',
...   'Philippines',
...   'Poland',
...   'Portugal',
...   'Qatar',
...   'Romania',
...   'Russia',
...   'Rwanda',
...   'Saint Kitts and Nevis',
...   'Saint Lucia',
...   'Saint Vincent and the Grenadines',
...   'Samoa',
...   'San Marino',
...   'Sao Tome and Principe',
...   'Saudi Arabia',
...   'Senegal',
...   'Serbia',
...   'Seychelles',
...   'Sierra Leone',
...   'Singapore',
...   'Slovakia',
...   'Slovenia',
...   'Solomon Islands',
...   'Somalia',
...   'South Africa',
...   'South Sudan',
...   'Spain',
...   'Sri Lanka',
...   'Sudan',
...   'Suriname',
...   'Sweden',
...   'Switzerland',
...   'Syria',
...   'Tajikistan',
...   'Tanzania',
...   'Thailand',
...   'Togo',
...   'Tonga',
...   'Trinidad and Tobago',
...   'Tunisia',
...   'Turkey',
...   'Turkmenistan',
...   'Tuvalu',
...   'Uganda',
...   'Ukraine',
...   'United Arab Emirates',
...   'United Kingdom',
...   'United States',
...   'Uruguay',
...   'Uzbekistan',
...   'Vanuatu',
...   'Vatican City',
...   'Venezuela',
...   'Vietnam',
...   'Yemen',
...   'Zambia',
...   'Zimbabwe'
... ];
>>> for country in countries:
...     if 'land' in country:
...             print(country)
...
Finland
Iceland
Ireland
Marshall Islands
Netherlands
New Zealand
Poland
Solomon Islands
Switzerland
Thailand
>>> fruits = ['banana', 'orange', 'mango', 'lemon']
>>> for i in range(len(fruits)-1, -1, -1):
...     print(fruits[i])
...
lemon
mango
orange
banana
