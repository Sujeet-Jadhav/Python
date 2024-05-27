# Logger example
#importing module
import logging

#Create and configure logger
logging.basicConfig(filename="newfile.log", format='%(asctime)s %(message)s', filemode='w')

#Creating an object
logger=logging.getLogger()

#Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

#Test messages
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")

logging.basicConfig(level=logging.WARNING)

def hypotenuse(a, b):
    """Compute the hypotenuse"""
    return (a**2 + b**2)**0.5

kwargs = {'a':3, 'b':4, 'c':hypotenuse(3, 4)}

logging.debug("a = {a}, b = {b}".format(**kwargs))
logging.info("Hypotenuse of {a}, {b} is {c}".format(**kwargs))
logging.warning("a={a} and b={b} are equal".format(**kwargs))
logging.error("a={a} and b={b} cannot be negative".format(**kwargs))
logging.critical("Hypotenuse of {a}, {b} is {c}".format(**kwargs))

#> WARNING:root:a=3 and b=3 are equal
#> ERROR:root:a=-1 and b=4 cannot be negative
#> CRITICAL:root:Hypotenuse of a, b is 5.0