# str.strip(): it removes given characters(or whitespaces if no character involved) begining from the end and beginning 
# until it does not match with given character
string = '   www.example.com   '
string = string.strip() #removes whitespaces
string = string + "   d"
string = string.strip()

string = string.strip('.weacmd').strip() 

comment_string = '#....... Section 3.2.1 Issue #32 .......'
comment_string = comment_string.strip('.#! ')

a = 11