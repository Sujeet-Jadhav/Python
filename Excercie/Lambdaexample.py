# This is a lambda function which is also called as anonymous functions.
x = lambda x: x*x
print(x(4))

# Using paranthesis for providing the arguments.
print((lambda x: x*x)(5))

# It can take any number of arguments
print((lambda x, y, z: x*y*z)(5, 8, 2))

# What does lambda function return
string1 = 'example for lambda function'
print(lambda string1 : print(string1))
# This is because it returns a function object.

# Here we are making an immediate call to the function by passing the argument.
# This is also called as immediately invoked function execution

(lambda string2 : print(string2))('This is another example of lambda')

# Lambda functions with filter(). This works for any constraint to be applied.
sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = filter(lambda x: x < 4, sequences)
print(list(filtered_result))

# Lambda functions with map(). This is used when an operation is to be performed
sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = map(lambda x: x*x, sequences)
print(list(filtered_result))

# example of docstring
def my_function():
	"""Demonstrates triple double quotes
	docstrings and does nothing really."""

	return None

print("Using __doc__:")
print(my_function.__doc__)

print("Using help:")
help(my_function)

# example of multiline docstrings

def my_function(arg1):
    """
    Summary line.

    Extended description of function.

    Parameters:
    arg1 (int): Description of arg1

    Returns:
    int: Description of return value

    """

    return arg1


print(my_function.__doc__)

# indentation in docstring
class ComplexNumber:
    """
    This is a class for mathematical operations on complex numbers.

    Attributes:
        real (int): The real part of complex number.
        imag (int): The imaginary part of complex number.
    """

    def __init__(self, real, imag):
        """
        The constructor for ComplexNumber class.

        Parameters:
        real (int): The real part of complex number.
        imag (int): The imaginary part of complex number.
        """

    def add(self, num):
        """
        The function to add two Complex Numbers.

        Parameters:
            num (ComplexNumber): The complex number to be added.

        Returns:
            ComplexNumber: A complex number which contains the sum.
        """

        re = self.real + num.real
        im = self.imag + num.imag

        return ComplexNumber(re, im)


help(ComplexNumber)  # to access Class docstring
help(ComplexNumber.add)  # to access method's docstring

# example of map function
def square(n : int)-> int:
    return n * n

my_list = [2,3,4,5,6,7,8,9]
updated_list = map(square, my_list)
print(updated_list)
print(list(updated_list))


print(square.__annotations__)