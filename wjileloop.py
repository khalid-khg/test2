num_of_tries = 0
while num_of_tries != 3:
    username = input('please insert your username: ')
    password = input('please insert your password: ')
    if username == 'khalid' and password == '1234' :
        print('Welcome')
        unm_of_tries = 0
        exit()
    else:
        print('error')
        num_of_tries +=1
        print('you have ' + str(3 - num_of_tries) + " tries left")