

"""
Student Management System (object oriented programming)
- terminal based

"""


from student_class import student
from os import system

student_list = []

while True:

    print("\n-----------------------------------")
    print('1. Add student')
    print('2. Show student')
    print('3. Remove student')
    print('4. Edit student')
    print('5. Exit')
    print("-----------------------------------\n")

    menu = input('Menu: ')
    system('cls')

    match menu:

        case '1':
            
            firstname = input('firstname: ')
            lastname = input('lastname: ')
            age = input('age: ')
            gender = input('gender: ')
            
            while True:
                nationalcode = input('nationalcode: ')

                for std in student_list:
                    if std.nationalcode == nationalcode:
                        print(f'{nationalcode} exists!')
                        break
                
                else:
                    break

            while True:
                stdcode = input('stdcode: ')

                for std in student_list:
                    if std.stdcode == stdcode:
                        print(f'{stdcode} exists!')
                        break
                
                else:
                    break

            instance = student(firstname, lastname, age, gender, nationalcode, stdcode)
            student_list.append(instance)

            system('cls') 

        case '2':
            #region show list
            print("____________________________________________________________________________________________\n")

            for student in student_list:
                print(student.show_std())
                    
            print("____________________________________________________________________________________________\n")
            #endregion

        case '3':
            
            #region show list
            print("____________________________________________________________________________________________\n")

            for student in student_list:
                print(student.show_std())
                
            print("____________________________________________________________________________________________\n")
            #endregion

            remove = input('Enter the student code of the one who you want to remove: ')
            system('cls')

            check_exists = False

            for std in student_list:
                if std.stdcode == remove:
                    check_exists = True  
                    student_list.remove(std)
                    print('Done.')

                else:
                    system('cls')

            if not check_exists:
                print('This student does not exist.')

        case '4':
             #region show list
            print("____________________________________________________________________________________________\n")

            for student in student_list:
                print(student.show_std())
                    
            print("____________________________________________________________________________________________\n")
            #endregion    

            edit = input('Enter the data you want to edit: ')
            system('cls')

            check_exists = False

            for std in student_list:
                if std.firstname == edit:
                    check_exists = True  
                    std.firstname = input('enter new firstname: ')
                
                elif std.lastname == edit:
                    check_exists = True  
                    std.lastname = input('enter new lastname: ')
                
                elif std.age == edit:
                    check_exists = True  
                    std.age = input('enter new age: ')
                
                elif std.gender == edit:
                    check_exists = True  
                    std.gender = input('enter new gender: ')
                
                elif std.nationalcode == edit:
                    check_exists = True  
                    std.nationalcode = input('enter new national code: ')
                
                elif std.stdcode == edit:
                    check_exists = True  
                    std.stdcode = input('enter new student code: ')

                else:
                    system('cls')

                if check_exists:
                    print('Done.')

            if not check_exists:
                print('This student does not exist.')
            
        case '5':
            break
