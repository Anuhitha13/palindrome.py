string = input('enter the string:')
rev_string = string[ : : -1]
print('reversed string:',rev_string)
if string == rev_string:
    print('string is palindrome')
else:
     print('string is not a palindrome')