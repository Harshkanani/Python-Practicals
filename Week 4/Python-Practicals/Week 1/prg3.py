def add(i1, i2):
    sum = 0
    for i in range(0, i2):
        sum = sum + i1
    print("Sum = ", sum)

i1 = int(input("Enter a number for multiplication: "))
i2 = int(input("Enter another number for multiplication: "))
add(i1, i2)