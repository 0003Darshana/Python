import re
form = "^[a-z0-9.]+@gmail.com"
if re.match(form,input('Enter Google gmail : ')):
    print(f'Welldone!!! {chr(128516)}')
else:
    print(f'Alien {chr(128125)}')
