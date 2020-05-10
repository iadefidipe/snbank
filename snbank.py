import random
program_option = input('Would you like to login: ').lower()

print('Please login')
while program_option == 'l':
    username = input('Please Enter your Username: ')
    password = input('Please Enter your Password: ')
    file= open("staff.txt","r")
    Staff_file = file.readline()
    for word in Staff_file:
        line = Staff_file.split()
        print(Staff_file)
        username1 = (line [0])
        password1 = (line [1])

        if username == username1 and password == password1:
            print("Login sucessful")

            session = open("session.txt","w+")
            for i in range (1):
                session.write('User logged in')
            session.close()
            while True:
                    staff_choice =int(input('''Press 1 to create account
Press 2 to Check Account Details
Press 3 to Log out'''))
                    if staff_choice == 1:
                        account_name = input('Please input desired accunt name: ')
                        opening_bal = input('Your opening balance: ')
                        account_type = input('Desired account type: ')
                        account_email = input('Email: ')
                        account_no= None
                        for i in range(10):
                            account_no = random.randint(0000000000,9999999999)
                        customer_file = open("Customer.txt", 'w+')
                        customer_file.write('Account name: %s \n' %account_name)
                        customer_file.write('Opening balance: %s \n' % opening_bal)
                        customer_file.write('Account type: %s \n' % account_type)
                        customer_file.write('Account email: %s \n' % account_email)
                        customer_file.close()
                        print(f'This is your account number: {account_no}')
                        continue

                    elif staff_choice == 2:
                        while True:

                                account_noVerify = int(input('Please input you account number: '))
                                if account_noVerify == account_no:
                                    customer_file = open('customer.txt','r')
                                    for customer in (customer_file):
                                        customer = customer.split('\n')
                                        print(customer)
                                    continue
                                else:
                                    print('please Try again')
                                    continue

                    if staff_choice == 3:
                        print('Logging Out')
                    break








            break
            file.close()


        else:
            print('Wrong details. Try again')
            file.close()
