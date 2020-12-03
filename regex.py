# https://www.w3schools.com/python/python_regex.asp

import re
str = 'some text for test regex 2020 !'

print(re.search('for', str))

t = re.search('for', str)
print(t.start())

# -------------------------------------

pattern = re.compile('for')
a = pattern.search(str)
print(a.group())