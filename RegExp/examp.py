https://habr.com/ru/post/349860/
>>> import re
>>> result = re.match(r'AV', 'AV Analytics Vkjhkjh AV')
>>> print result
<_sre.SRE_Match object at 0xb5e74d78>
>>> print result.group(0)
AV
# python2

>>> match = re.search(r'\d\d\D\d\d', r'Телефон 123-12-12')
>>> print match.group(0)
23-12

# python3
import re 
match = re.search(r'\d\d\D\d\d', r'Телефон 123-12-12') 
print(match[0] if match else 'Not found') 
# -> 23-12 
