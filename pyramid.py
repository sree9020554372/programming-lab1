rows = int (input("enter values"))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(i * j, end=' ')
    print()