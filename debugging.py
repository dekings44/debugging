# First step in debugging is to Describe the problem


# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print('You got it')

# my_function()

'''
In the function above, it is expected that i is meant to print You got it
but it does print it.

When looked, the way range works is that it runs from a lower limit
to one less than the upper limit.
The upper limit here is 20, hence it never gets to 20. The condition will never
be met.
'''

# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print('You got it')

# my_function()

#Second Reproducing the bug

# from random import randint
# dice_imgs = ['😴', '😥', '🤑', '😷', '🤓', '😭', '😍']
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

'''
The above code works, however, it occasionally produce error.
so here, when the code is run with dice_num giving from 1 to 6
a number at a time, when it gets to 6, it says out of range.
This is true because the list is zero indexed.Everything works until
it gets to the index 6.
To fix, this we either increase the item in the list or reduce the randint
input to 5.

'''

# from random import randint
# dice_imgs = ['😴', '😥', '🤑', '😷', '🤓', '😭']
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# Third, Play Computer

# year = int(input('What is your year of birth? '))

# if year > 1980 and year < 1994:
#     print('You are a millenial.')
# elif year > 1994:
#     print('You are a Gen Z')

'''
This code will return nothing when 1994 is entered
This is because 1994 was not captured
A simple stricter equality sign for 1994 will capture it.
'''

'''
PRINT IS YOUR FRIEND

The use of print is a very effective and friendly way
to debug errors line after line.
It help you see errors that your IDE and console could not capture
'''

# Using A Debugger Tool

# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#     b_list.append(new_item)
#     print(b_list)

# mutate([1, 2, 3, 5, 8, 13])

'''
Using the debugger it is very clear that the b_list is empty
following the block code it belongs to
'''

# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)

# mutate([1, 2, 3, 5, 8, 13])


# TAKE A BREAK

# ASK A FRIEND

# RUN YOUR CODE OFTEN.

# STACKOVERFLOW