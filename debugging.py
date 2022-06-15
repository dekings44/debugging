# First step in debugging is to Describe the problem


def my_function():
    for i in range(1, 20):
        if i == 20:
            print('You got it')

my_function()

'''
In the function above, it is expected that i is meant to print You got it
but it does print it.

When looked, the way range works is that it runs from a lower limit
to one less than the upper limit.
The upper limit here is 20, hence it never gets to 20. The condition will never
be met.
'''

def my_function():
    for i in range(1, 21):
        if i == 20:
            print('You got it')

my_function()