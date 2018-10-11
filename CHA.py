# First fun program

#######################
# Users
#######################
JOSH = 'Josh'
DEREK = 'Derek'


#######################
# Python conventions
#######################
CONSTANTS = 'Never going to change'
this_is_a_variable = 'Something that could change'


def is_same_name(name1, name2):
    return name1.lower() == name2.lower()


print ('Hello, please enter your company provided user ID')
userID = input()
if len(userID) > 0:
    print ('Hello, ' + userID) 
    if is_same_name(userID, DEREK):
        print ('Welcome back. You are a good programmer.')
    elif is_same_name(userID, JOSH):
        print ('Welcome back. You will be a good programmer very soon.')
    else:
        print("Um... I don't know you dude")
else:
    print('You need to tell me your damn USER ID!')
