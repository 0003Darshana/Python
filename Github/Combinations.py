def fact(n):
    if n == 0:
        return 1
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f

def combinations(string, r, comb_str='', k=0):
    if r == 0:
        print(comb_str)
        return
    for i in range(k, len(string)):
        combinations(string, r - 1, comb_str + string[i], i + 1)

def main():
    string = input("Enter your string for performing combinations with string's characters: ")
    n = len(string)
    for r in range(1, len(string) + 1):
        nc = fact(n) // (fact(r) * fact(n - r))
        print('\nNo. of combinations possible with %d length = %d' % (r, nc))
        combinations(string, r)

if __name__ == "__main__":
    main()
