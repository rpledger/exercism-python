#
# Skeleton file for the Python "Hello World" exercise.
#


def hello(name=''):
    if not name:
    	greeting = "Hello, World!"
    else:
    	greeting = "Hello, %s!" % (name)
    return greeting
