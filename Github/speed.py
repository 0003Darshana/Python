n=int(input('Enter the speed : '))
def speed(n):
    demerit = 0
    d = 0
    if n < 70:
        print('OK')
    else:
        d = n - 70
        e = d//5
        for i in range(e):
            demerit += 1
    return demerit
demerits = speed(n)
if demerits >= 12:
    print('License suspended')
elif demerits > 0:
    print(demerits)


