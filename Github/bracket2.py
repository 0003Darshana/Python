string=input("Enter brackets of strings : ")
open_brackets=[]
flag=True
for char in string:
  if char in ('{','[','('):
    open_brackets.append(char)
  elif char == '}' and open_brackets[-1] == '{' :
    open_brackets.pop()
  elif char == ']' and open_brackets[-1] == '[' :
    open_brackets.pop()
  elif char == ')' and open_brackets[-1] == '(' :
    open_brackets.pop()
  else:
    print('Your input string is not acceptable')
    flag=False
    break
if flag:
  if open_brackets: # if empty list, then by default the condition is False otherwise True
    print('Invalid')
  else:
    print('Valid')
else:
  print('Make your input as right?')
