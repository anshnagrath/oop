class MissingLabelError(KeyError):
    pass

class PageNotFoundError(LookupError):
    pass

class IncorrectPasswordError(ValueError):
    pass

class IncorrectUsernameError(ValueError):
    pass 

class APIThrottleError(RuntimeError):
    pass

def login():
   raise IncorrectPasswordError
try:
    login()
except IncorrectPasswordError:
    print('incorrect username error have you forgot it')

