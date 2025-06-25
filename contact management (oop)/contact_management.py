
"""
Contact Management System (object oriented programming)
- terminal based

"""


from contact_class import contact
from os import system

contact_list = []

while True:

    print("\n-----------------------------------")
    print('1. Add contact')
    print('2. Show contact')
    print('3. Remove contact')
    print('4. Edit contact')
    print('5. Exit')
    print("-----------------------------------\n")

    menu = input('Menu: ')
    system('cls')

    match menu:

        case '1':
            
            firstname = input('firstname: ')
            lastname = input('lastname: ')
             
            while True:
                phone = input('phone: ')

                for cnt in contact_list:
                    if cnt.phone == phone:
                        print(f'{phone} exists!')
                        break
                
                else:
                    break

            gender = input('gender: ')
            description = input('description: ')

            instance = contact(firstname, lastname, phone, gender, description)
            contact_list.append(instance)

            system('cls') 

        case '2':
            #region show list
            print("____________________________________________________________________________________________\n")

            for cnt in contact_list:
                print(contact.show_contact(cnt))
                    
            print("____________________________________________________________________________________________\n")
            #endregion

        case '3':
            
            #region show list
            print("____________________________________________________________________________________________\n")

            for cnt in contact_list:
                print(contact.show_contact(cnt))
                    
            print("____________________________________________________________________________________________\n")
            #endregion

            remove = input('Enter the phone number of the one you want to remove: ')
            system('cls')

            check_exists = False

            for cnt in contact_list:
                if cnt.phone == remove:
                    check_exists = True  
                    contact_list.remove(cnt)
                    print('Done.')

                else:
                    system('cls')

            if not check_exists:
                print('This contact does not exist.')

        case '4':
             #region show list
            print("____________________________________________________________________________________________\n")

            for cnt in contact_list:
                print(contact.show_contact(cnt))
                    
            print("____________________________________________________________________________________________\n")
            #endregion    

            edit = input('Enter the phone number of the one you want to edit: ')
            system('cls')

            check_exists = False

            for cnt in contact_list:
                if cnt.phone == edit:
                    check_exists = True  
                    
                    print('1. firstname   2. lastname    3. phone    4. gender    5. description')
                    edit_option = input('Enter the number you want to change:')
                    match edit_option:
                        case '1':
                            cnt.firstname = input('enter new firstname: ')
                        case '2':
                            cnt.lastname = input('enter new lastname: ')
                        case '3':
                            cnt.phone = input('enter new phone: ')
                        case '4':
                            cnt.gender = input('enter new gender: ')
                        case '5':
                            cnt.description = input('enter new description: ')
                        case _:
                            print('invalid option!!!')


                    print('Done.')

                else:
                    system('cls')

            if not check_exists:
                print('This contact does not exist.')
            
        case '5':
            break
