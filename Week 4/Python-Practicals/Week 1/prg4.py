phone_no = input("Enter a phone number : ")
length = len(phone_no)
is_Valid = False
if(length == 12):
    for i in range(0, length-1):
        if((i == 3 or i == 7) and phone_no[i] == "-"):
            is_Valid = True
        elif(phone_no[i].isdigit()):
            is_Valid = True
        else:
            is_Valid = False
            break
else:
    is_Valid = False

if(is_Valid):
    print("Valid Phone Number.")
else:
    print("Invalid Phone Number.")