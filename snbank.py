import random
program_option = input('''What can I do for you today? 
To Login, Type 'Login'
''').lower()

while program_option == 'login':
    username = input('Please Enter your Username: ')
    password = input('Please Enter your Password: ')
    file = open("staff.txt","r")
    read_file = file.read()
    Staff_file = read_file.split('\n')
    for word in Staff_file:
        line = word.rsplit()
        username1 = (line [0])
        password1 = (line [1])

        if username == username1 and password == password1:
            print("Login sucessful")

            session = open("session.txt","w+")
            for i in range (1):
                session.write(f'User logged in: {username1}')
            session.close()
            while True:
                    staff_choice =int(input('''Press 1 to create account
Press 2 to Check Account Details
Press 3 to Log out'''))
                    if staff_choice == 1:
                        account_name = input('Please input desired account name: ')
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
                                    break
                

                                else:
                                    print('please Try again')
                                    continue

                    if staff_choice == 3:
                        print('Logging Out')
                        del session
                    break








            break
            file.close()

else:
    print('Wrong details. Try again')
    file.close()

