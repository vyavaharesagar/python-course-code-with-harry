import re

mystr = '''We currently maintain 622 data sets as a service to the machine learning community. 
You may view all data sets through our searchable interface. 
For a general overview of the Repository, please visit our About page. 
For information about citing data sets in publications, please read our citation policy. 
If you wish to donate a data set, please consult our donation policy. For any other questions, 
feel free to contact the Repository librarians.'''

# findall,split, search, sub, finditer

# patt = re.compile(r'.ble')
# patt = re.compile(r'^Re')
patt = re.compile(r'ans.$')


matches = patt.finditer(mystr)
for match in matches:
    print(match)