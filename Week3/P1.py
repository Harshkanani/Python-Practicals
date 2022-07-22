def add_student(name):
    file = open('students.txt', 'a')
    file.write(name+'\n')
    file.close()

def find_student(name):
    file = open('students.txt', 'r')
    index = 0
    for line in file.readlines():
        index += 1
        if line.strip() == name:
            file.close()
            print('Student found at line ', index)
        else:
            file.close()
            print('Student not found!')

def display_students():
    file = open('students.txt', 'r')
    for student in file.readlines():
        print('Student Name = ', student)


while True:
    print('[1] Add Student.')
    print('[2] Find Student.')
    print('[3] Display Student.')
    print('[4] Exit.')
    choice = int(input('Enter Choice -> '))
    if(choice == 1):
        add_student(input('Enter Student Name -> '))
    elif(choice == 2):
        find_student(input('Enter Student Name to Find -> '))
    elif(choice == 3):
        display_students()
    elif(choice == 4):
        break
    else:
        print('Invalid Choice')