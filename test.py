Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> da_phone_number = 0669320094
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> 
================================ RESTART: Shell ================================
>>> da_phone_number = "0669320094"
>>> da_phone_number
'0669320094'
>>> "tire" + "bouchon"
'tirebouchon'
>>> "tire-" + "bouchon"
'tire-bouchon'
>>> runSmartContract
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    runSmartContract
NameError: name 'runSmartContract' is not defined
>>> number > letter
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    number > letter
NameError: name 'number' is not defined
>>> page > letter
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    page > letter
NameError: name 'page' is not defined
>>> page = "4"
>>> 
>>> 
>>> 
>>> letter = 3
>>> letter
3
>>> page
'4'
>>> page=4
>>> page
4
>>> page=jjj
>>> page
3
>>> page>letter
False
>>> letter>page
False
>>> page
3
>>> letter
3
>>> letter=4
>>> page>letter
False
>>> letter>page
True
>>> characters=['filou', 'maman', 'david', 'papa']
>>> characters
['filou', 'maman', 'david', 'papa']
>>> my-dictionnary = {}
SyntaxError: cannot assign to operator
>>> 