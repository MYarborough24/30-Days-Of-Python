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
>>> ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
>>> ages.sort()
>>> print(ages)
[19, 19, 20, 22, 24, 24, 24, 25, 25, 26]
>>> print(min(ages))
19
>>> print(max(ages))
26
>>> middle1 = ages[len(ages) // 2-1]
>>> middle2 = ages[len(ages) // 2]
>>> median = (middle1 + middle2) / 2
>>> print(median)
24.0
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
>>> print(len(countries)
... )
195
>>> middle = ages[len(ages) // 2]
>>> median = middle / 2
>>> print(median)
12.0
>>> middle_country = countries[len(countries) // 2]
>>> print(middle_country)
Lesotho
>>> countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
>>> first, second, third, *scandic countries = countries
  File "<stdin>", line 1
    first, second, third, *scandic countries = countries
                                   ^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> first, second, third, *scandic_countries = countries
>>> print(scandic_countries)
['Finland', 'Sweden', 'Norway', 'Denmark']
