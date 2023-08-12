
s=input().split()
lst=list(s)
def w(s):
    a=len(lst[0])
    for i in lst:
        if len(i)>a:
            a=len(i)
            continue
    return a
print(w(s))
