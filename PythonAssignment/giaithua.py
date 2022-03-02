n = int(input("nhap so can tinh giai thua: "))
def gt(n):
    if n == 0:
        return 1;
    return n * gt(n-1)
print(gt(n))