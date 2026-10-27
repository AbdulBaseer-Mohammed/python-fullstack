Python 3.15.1 (tags/v3.15.1:c37e74c, Oct 21 2026, 06:24:08) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
5&14
4
11&12
8
11/12
0.9166666666666666
11|12
15
8|9
9
11^12
7
~11
-12
~90
-91
~17
-18
~34
-35
2<<2
8
2<<1
4
15>>1
7
16>>2
4
a = intput("Enter rhe string:")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a = intput("Enter rhe string:")
NameError: name 'intput' is not defined. Did you mean: 'input'?
a= intput("Enter rhe string:")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a= intput("Enter rhe string:")
NameError: name 'intput' is not defined. Did you mean: 'input'?
a= input("Enter rhe string:")
Enter rhe string:hello
a
'hello'
a =input()
678
type(a)
<class 'str'>
a = int(input())
243
a
243
a = int(input("enter the integer:")

    Enter the float:12
        
SyntaxError: '(' was never closed
a = int(input("enter the integer:"))
enter the integer:223
a = float(input("enter the integer:")
          124,55
          
SyntaxError: '(' was never closed
a = float(input("enter the integer:"))
enter the integer:333
a = float(input("enter the float:"))
enter the float:225.77
a = float(input("enter the float:"))
enter the float:33
a
33.0
a
33.0
a = list(input())
1224432334
a
['1', '2', '2', '4', '4', '3', '2', '3', '3', '4']
a = list(input())

12 23 2 4  46 67 866 65544 22244544 
a
['1', '2', ' ', '2', '3', ' ', '2', ' ', '4', ' ', ' ', '4', '6', ' ', '6', '7', ' ', '8', '6', '6', ' ', '6', '5', '5', '4', '4', ' ', '2', '2', '2', '4', '4', '5', '4', '4', ' ']
'12 23 2 4  46 67 866 65544 22244544 
'12 23 2 4  46 67 866 65544 22244544'.split('')
SyntaxError: unterminated string literal (detected at line 1)
'12 23 2 4  46 67 866 65544 22244544'.split('')
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    '12 23 2 4  46 67 866 65544 22244544'.split('')
ValueError: empty separator
a = list(input())
12345444562
a = list(input())
1223
a
['1', '2', '2', '3']
map (int,a)
<map object at 0x000002B4F7EED480>
list(map(int,a))
[1, 2, 2, 3]
a = list(map(int,a))
1 3 5 23 13353 5
SyntaxError: invalid syntax
1 33 53 12 333 556
SyntaxError: invalid syntax
a = list(map(int,intput().split()))
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a = list(map(int,intput().split()))
NameError: name 'intput' is not defined. Did you mean: 'input'?
a = list(map(int,intput().split()))
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a = list(map(int,intput().split()))
NameError: name 'intput' is not defined. Did you mean: 'input'?
a = list(map(int,a))

KeyboardInterrupt
a = list(map(int,a))
list(map(int,a))
[1, 2, 2, 3]
a = list(map(int,input().split()))
1 3 56 7 5 3 
a
[1, 3, 56, 7, 5, 3]
a = list(map(float,input().split()))
1 33 44 67 89 34 
a
[1.0, 33.0, 44.0, 67.0, 89.0, 34.0]
tuple of str - (input().string())
SyntaxError: invalid syntax
tuple str - (input().string())
SyntaxError: invalid syntax
a,b,c=(1,2,3)
a
1
b
2
3
3
a,b,c = list(map(int,input().split()))
1 2 3
a
1
b
2
c
3
email,password = input().split()
abdulbaseermohammes3@gmail.com 1234
email
'abdulbaseermohammes3@gmail.com'
password
'1234'
a,b,c = list(map(flot,input().split))
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a,b,c = list(map(flot,input().split))
NameError: name 'flot' is not defined. Did you mean: 'float'?
a,b,c = list(map(int,input().split()))

3 4 5 
a
3
b
4
c
5
a = eval(input))
SyntaxError: unmatched ')'
a = eval(input())
[1,2,3]
a
[1, 2, 3]
a =  eval(input())

Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    a =  eval(input())
  File "<string>", line 0
    
SyntaxError: invalid syntax
a =  eval(input())
"sdadsfadf"
a
'sdadsfadf'
a = eval(input())
(1,2,3)
True
True
a = eval(input))
SyntaxError: unmatched ')'
a = eval(input())
{1:1,2:2,3:4,5:6}
a = eval(input))
SyntaxError: unmatched ')'
a = eval(input())
True
a
True
a = eval(input())
2+5j
a
(2+5j)
a = eval(input())
12
a
12
a = eval(input())
12.4
SyntaxError: multiple statements found while compiling a single statement
a = eval(input())
12.3
SyntaxError: multiple statements found while compiling a single statement
a = 10
b = 10.2
c = "codegnan"
a
10
b
10.2
c
'codegnan'
print(a,b,c)
10 10.2 codegnan
print("a=",a,"b=",b,"c=",c)
a= 10 b= 10.2 c= codegnan
print("a=",a,"b=",b,"c=",c,sep='')
a=10b=10.2c=codegnan
print("a=",a,"b=",b,"c=",c,sep='-')

a=-10-b=-10.2-c=-codegnan
>>> print("a=",a,"b=",b,"c=",c,sep='\n\n')
... 
a=

10

b=

10.2

c=

codegnan
>>> print("a=",a,"b=",b,"c=",c,sep='@')
a=@10@b=@10.2@c=@codegnan
>>> print("a=",a,"b=",b,"c=",c,sep='@#@#')
a=@#@#10@#@#b=@#@#10.2@#@#c=@#@#codegnan
>>> print(f'a={a} b={b} c={c}')
a=10 b=10.2 c=codegnan
>>> print(f'a%=d b=%f c=%s'%(a,b,c))
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    print(f'a%=d b=%f c=%s'%(a,b,c))
ValueError: stray % at position 1 or unexpected format character '=' at position 2
>>> print('a%=d b=%f c=%s'%(a,b,c))
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    print('a%=d b=%f c=%s'%(a,b,c))
ValueError: stray % at position 1 or unexpected format character '=' at position 2
>>> print ('a=%d b=%f c=%s'%(a,b,c))
a=10 b=10.200000 c=codegnan
>>> print ('a=%d b=%2.f c=%s'%(a,b,c))
a=10 b=10 c=codegnan
>>> print('a={} b={};.format (a,b,c))
...       
SyntaxError: unterminated string literal (detected at line 1)
KeyboardInterrupt
>>> print('a={} b={}'.format (a,b,c))
a=10 b=10.2
>>> print('a={} b={}'.format (a,c,b))
a=10 b=codegnan
