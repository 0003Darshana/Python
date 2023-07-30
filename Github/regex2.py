import re
password = "^[A-Z][a-zA-Z0-5#@]{7}" #password chars > 7
if re.search(password,input('Enter : ')):
    print('Valid password')
else:
    print('Invalid')
