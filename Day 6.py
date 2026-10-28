Python 3.15.1 (tags/v3.15.1:c37e74c, Oct 21 2026, 06:24:08) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s = 'python'
s
'python'
p=''
p
''
s
'python'
t = 'programming'
s+t
'pythonprogramming'
t*3
'programmingprogrammingprogramming'
s*7
'pythonpythonpythonpythonpythonpythonpython'
'*'*20
'********************'
'(*_*)'*20
'(*_*)(*_*)(*_*)(*_*)(*_*)(*_*)(*_*)(*_*)(*_*)(*_*)(*_*)(*_*)(*_*)(*_*)(*_*)(*_*)(*_*)(*_*)(*_*)(*_*)'
;0;0*30
SyntaxError: invalid syntax
'0'*30
'000000000000000000000000000000'
'(^_^)'*20
'(^_^)(^_^)(^_^)(^_^)(^_^)(^_^)(^_^)(^_^)(^_^)(^_^)(^_^)(^_^)(^_^)(^_^)(^_^)(^_^)(^_^)(^_^)(^_^)(^_^)'
s = 'python java flask mysql fastapi'
s[0]
'p'
s[7]
'j'
s[-1]
'i'
s[-4]
't'
s[-7]
'f'
s[12]
'f'
'f'
'f'

s
'python java flask mysql fastapi'
s[0:6:1]
'python'
s[7:11:1]
'java'
s
'python java flask mysql fastapi'
s[:6]
'python'
s[7:11]
'java'

s[18:23]
'mysql'
s[24:]
'fastapi'
s[::-1]
'ipatsaf lqsym ksalf avaj nohtyp'
s[-7:]
'fastapi'
s[::2]
'pto aafakmslfsai'
s[-15:-20:-1]
'ksalf'
s[::-1]
'ipatsaf lqsym ksalf avaj nohtyp'
s[-5::-1]
'saf lqsym ksalf avaj nohtyp'
s[5::-1]
'nohtyp'
s
'python java flask mysql fastapi'
'java;
SyntaxError: unterminated string literal (detected at line 1)
'java'
'java'
'java' in s
True
'mysqul' in s
False
'c++' not on s
SyntaxError: invalid syntax
'c++' not on s
'c++' not in s
SyntaxError: invalid syntax
'c++' not in s
True
'python' not in s
False
s
'python java flask mysql fastapi'
len(s)
31
ord('a')
97
ord'(c')
SyntaxError: unmatched ')'
ord('c')
99
s
'python java flask mysql fastapi'
ord('*')
42
ord('%')
37
ord('g")
    
SyntaxError: unterminated string literal (detected at line 1)
ord('g')
103
ord('y')
121
ord('y+e')
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    ord('y+e')
TypeError: ord() expected a character, but string of length 3 found
chr(100)
'd'
chr(50)
'2'
chr(90)
'Z'
chr(783)
'̏'
chr(999)
'ϧ'
chr(80786)
'𓮒'
s
'python java flask mysql fastapi'
min(s)
' '
sorted(s)
[' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'f', 'f', 'h', 'i', 'j', 'k', 'l', 'l', 'm', 'n', 'o', 'p', 'p', 'q', 's', 's', 's', 't', 't', 'v', 'y', 'y']
s .upper()
'PYTHON JAVA FLASK MYSQL FASTAPI'
s.lower()
'python java flask mysql fastapi'
s.swapcase
<built-in method swapcase of str object at 0x000002334DCE7640>
s.swapcase()
'PYTHON JAVA FLASK MYSQL FASTAPI'
s.title()
'Python Java Flask Mysql Fastapi'
s.capitliaze()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    s.capitliaze()
AttributeError: 'str' object has no attribute 'capitliaze'. Did you mean '.capitalize' instead of '.capitliaze'?
s.capitalize()
'Python java flask mysql fastapi'
s.casefold()
'python java flask mysql fastapi'
s ='python'
s
'python'
s.center(40,'_')
'_________________python_________________'
s.center(40," ")
'                 python                 '
s.center(40,'*')
'*****************python*****************'
s.ljust(40,'^')
'python^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'
s.rjudt(40,'^')
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    s.rjudt(40,'^')
AttributeError: 'str' object has no attribute 'rjudt'. Did you mean '.rjust' instead of '.rjudt'?
s.rjust(40,'^')
'^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^python'
'1'.zfill(6)
'000001'
'123'.zfill(6)
'000123'
'123456788'.zfill(6)
'123456788'
s
'python'
s = python java flask mysql fastapi
SyntaxError: invalid syntax
s = 'python java flask mysql fastapi'
s
'python java flask mysql fastapi'
s,find('y')
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    s,find('y')
NameError: name 'find' is not defined
s.find('y')
1
s.find('z')
-1
s.find('a')
8
s.find('d')
-1
>>> s.find('h')
3
>>> s.find('p')
0
>>> s.find('b')
-1
>>> s = '            codeg   nan               '
>>> s.strip()
'codeg   nan'
>>> s.lstrip()
'codeg   nan               '
>>> s.rstrip()
'            codeg   nan'
>>> s ='python java flask mysql fastapi'
>>> s
'python java flask mysql fastapi'
>>> s.replace('a','*')
'python j*v* fl*sk mysql f*st*pi'
>>> s.replace('p','1')
'1ython java flask mysql fasta1i'
>>> maket rans('apkqs','12345')
SyntaxError: invalid syntax
>>> s.maket rans('apkqs','12345')
SyntaxError: invalid syntax
>>> s.maketrans('apkqs','12345')
{97: 49, 112: 50, 107: 51, 113: 52, 115: 53}
>>> s.translate(s.maketrans('apkqa','12345'))
'2ython j5v5 fl5s3 mys4l f5st52i'
>>> s.translate(s.maketrans('apkqa','*******'))
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    s.translate(s.maketrans('apkqa','*******'))
ValueError: the first two maketrans arguments must have equal length
>>> s.translate(s.maketrans('apkqa','****'))
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    s.translate(s.maketrans('apkqa','****'))
ValueError: the first two maketrans arguments must have equal length
>>> s.translate(s.maketrans('aeiou','*****'))
'pyth*n j*v* fl*sk mysql f*st*p*'
