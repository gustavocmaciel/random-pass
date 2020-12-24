import random

def generate_password(length):
    '''
    Generates a new password

    Argument: 
        number {integer} -- length of the password
    
    Returns:
        [string] -- the new password
    '''
    
    # Make sure the generated password will have the desired length
    ## FIXME: Check if is necessary to convert to int
    pass_length = int(length) - 3

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    special_characters = ['!','@','#','$','%','&','*']

    pass_list = []

    # Get a random letter from alphabet, convert to uppercase and append to pass_list
    random_letter = random.choices(alphabet)
    letter = ''.join(random_letter)
    upper_letter = letter.capitalize()
    pass_list.append(upper_letter)

    # Get a random special character and append to pass_list
    random_special = random.choices(special_characters)
    special = ''.join(random_special)
    pass_list.append(special)

    # Get a random numbert and append to pass_list
    random_number = random.choices(numbers)
    number = ''.join(random_number)
    pass_list.append(number)

    # Get random letters from alphabet and append to pass_list
    for i in range (int(pass_length)):
        random_item = random.choices(alphabet)
        item = ''.join(random_item)
        pass_list.append(item)

    # Convert pass_list to str
    password = ''.join(pass_list)

    return password
