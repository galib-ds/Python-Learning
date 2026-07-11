str = '''
this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE withing
the variable assignment will also show up.
'''
print(str)
# use of raw string
# first \ will be used for escaping
print('C:\\demo')
# raw string ignores escape character
print(r'C:\\demo')

print('/user/bin')