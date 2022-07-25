def table(n):
    for y in range(1, 11):
        for x in range(1, n + 1):
            print(y*x, end ="\t")
        print()

table(int(input("Enter the number of tables you want to display : ")))