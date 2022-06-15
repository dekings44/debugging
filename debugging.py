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

from random import randint
dice_imgs = ['😴', '😥', '🤑', '😷', '🤓', '😭', '😍']
dice_num = randint(1, 6)
print(dice_imgs[dice_num])

'''
The above code works, however, it occasionally produce error.
so here, when the code is run with dice_num giving from 1 to 6
a number at a time, when it gets to 6, it says out of range.
This is true because the list is zero indexed.Everything works until
it gets to the index 6.
To fix, this we either increase the item in the list or reduce the randint
input to 5.

'''

from random import randint
dice_imgs = ['😴', '😥', '🤑', '😷', '🤓', '😭']
dice_num = randint(1, 6)
print(dice_imgs[dice_num])