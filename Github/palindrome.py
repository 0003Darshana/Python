a=input('Enter : ')
b=''.join(reversed(a))
print('palindrome' if b==a else 'not')


c = input("Enter a string: ")
d = ''
for i in range(len(c)-1, -1, -1):
    d += c[i]
print(d)

e=input("Enter a string: ")
f=e[::-1]
print(f)
