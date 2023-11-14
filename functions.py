# Functions:
# Not all functions return a value
x = print('hello')
print(x)


# Custom functions can also return or not a value
"""This function return a value so when we call the function
 then we get a value"""
def foo():
	value = 10
	return value


x = foo()
print(x)


"""This function does not return a value so when we call the function
 then we get nothing"""
def foo():
	value = 10

x = foo()
print(x)


# Return Vs Print
def foo1():
	value = 10
	return value

x = foo1()
print(x)
