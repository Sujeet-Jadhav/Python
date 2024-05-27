# import module sys to get the type of exception
import sys
randomList = ['a', 0, 2]
for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    # except Exception as e:  # every exception inherits from base class Exception
    #     print("Oops!", e.__class__, "occurred.")
    #     # except:
    #     #     print("Oops!", sys.exc_info()[0], "occurred.")
    #     # the exc_info() function inside sys module prints the name of the exception
    except (ValueError):
        pass
    except (TypeError, ZeroDivisionError):
        print("Oops!", sys.exc_info(), "occurred.")
        print("Next entry.")
        print()
