#! python3
# 测试程序：匹配每3位就有一个逗号的数字。
import re
#numRegex=re.compile(r'\d{1,3}(,\d{3})*$')
numRegex=re.compile(r'(^(\d{1,3}))((,\d{3})*$)')
str='2,346,456,545,788,677'
mo=numRegex.search(str)
print(mo.group(0))
