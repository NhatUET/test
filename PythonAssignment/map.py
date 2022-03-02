n = int(input("nhap n: "))
dictNum = dict()
for i in range (1, n+1):
    dictNum[i] = i * i;
print('\n'.join(str(dictNum).split(",")))