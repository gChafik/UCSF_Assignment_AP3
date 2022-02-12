
with open("./Input/users.csv") as users_input:
    users_input_lst = users_input.readlines()
    print(users_input_lst)
    users_abc = [user.rstrip('\n') for user in users_input_lst[1:] if user.rstrip('\n').endswith('@abc.edu')]
    # for user in users_input_lst[1:]:
    #     print(user)
    #     if user.endswith('@abc.edu'):
    #         print(user)
    #         users_abc.append(user)
    print(users_abc)


with open('user_outlput.csv', 'a') as users_output:
    for user in users_abc:
        users_output.write(f"{user}\n")
