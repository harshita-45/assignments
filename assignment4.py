ch = input("Enter an alphabet: ").upper()
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = alphabets.index(ch) + 1

for i in range(n, 0, -1):
    left = alphabets[:i]
    right = alphabets[i-1::-1]
    spaces = " " * (2*(n-i)-1)
    if i == n:
        print(left + right[1:])
    else:
        print(left + spaces + right)


