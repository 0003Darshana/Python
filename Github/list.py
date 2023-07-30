lst_len = int(input('Enter the no.of elements in the list : '))

def lst(lst_len):
    lst_ele = []
    for i in range(lst_len):
        a = int(input('Enter the list element : '))
        lst_ele.append(a)
    lst_ele.sort()
    return lst_ele

def view(lst_ele):
        
        x = slice(-2,-1)
        y = lst_ele[x]
        for i in y:
            print(i)
        return y


print(view(lst(lst_len)))


