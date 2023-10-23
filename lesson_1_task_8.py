
#1
def num(line, count=0):
    if count < 11:
        print(line)
        return num(line + 1, count + 1)
    else:
        return line

result = num(88005553525)

print("_______________________")
#2
def num(a, b, c, d, e, f, g, h, m, n, o):
    print("line  1:", a + b + c)
    print("line  2:", a + b + c + d)
    print("line  3:", a + b + c + d + e)
    print("line  4:", a + b + c + d + e + f)
    print("line  5:", a + b + c + d + e + f + g)
    print("line  6:", a + b + c + d + e + f + g + f)
    print("line  7:", a + b + c + d + e + f + g + f + g)
    print("line  8:", a + b + c + d + e + f + g + f + g +h)
    print("line  9:", a + b + c + d + e + f + g + f + g +h + m)
    print("line 10:", a + b + c + d + e + f + g + f + g +h + m + n)
    print("line 11:", a + b + c + d + e + f + g + f + g +h + m + n + o)

num(80000000000, 6000000000, 1000000000, 1000000000, 5000000, 500000, 50000, 3000, 500, 30, 5)






