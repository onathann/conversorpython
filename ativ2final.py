def printdecimal(num):
    print(num, end='                         ')


def printoctal(num):
    print(oct(num), end='                       ')


def printhexadecimal(num):
    print(hex(num), end='                       ')


def printbinario(num):
    print(bin(num))


def lista():
    print("Decimal ---------------- octal ---------------- hexadecimal ---------------- binário")


lista()

for c in range(0, 225):
    printdecimal(c)
    printoctal(c)
    printhexadecimal(c)
    printbinario(c)