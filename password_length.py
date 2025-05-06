user_name = input('Please enter the User name : ')
pass_word = input('Please enter the new password: ')
pass_length = len(pass_word)
hidden_pass = '*' * pass_length
print(f'Hey..! {user_name} your password {hidden_pass} is {pass_length} letters long')
