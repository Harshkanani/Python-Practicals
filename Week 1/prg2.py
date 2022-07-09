def return_inch(feet):
    return feet*12

def print_feet(feet):
    return feet

def print_inch(inch):
    return inch

def calc_height(i1):
    feet = int (i1 / 12)
    inch = i1 % 12
    print("Feet = ", feet, "Inch = ", inch)

inp = int(input("Enter Feet : "))
print("Inches = ", return_inch(inp))

inp2 = int(input("Enter Feet : "))
print("Feet = ", print_feet(inp2))

inp3 = int(input("Enter Inch : "))
print("Inch = ", print_inch(inp3))

calc_height(inp3)