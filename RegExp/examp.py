>>> import re
>>> result = re.match(r'AV', 'AV Analytics Vkjhkjh AV')
>>> print result
<_sre.SRE_Match object at 0xb5e74d78>
>>> print result.group(0)
AV
