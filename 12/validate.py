from collections import namedtuple

User = namedtuple('User', 'name role expired')
USER, ADMIN = 'user', 'admin'
SECRET = 'I am a very secret token'

julian = User(name='Julian', role=USER, expired=False)
bob = User(name='Bob', role=USER, expired=True)
pybites = User(name='PyBites', role=ADMIN, expired=False)
USERS = (julian, bob, pybites)

# define exception classes here

class UserDoesNotExist(Exception):
    """Raised when the user is not in USERS"""
    pass

class UserAccessExpired(Exception):
    """Raised when the user is expired"""
    pass

class UserNoPermission(Exception):
    """Raised when the user is not admin"""
    pass

def get_secret_token(username):
    """
        Create a function that takes a username and checks for a valid user:

        The username is in USERS,
        the user is not expired, and
        the user has the ADMIN role.
        If those 3 conditions are met return SECRET.

        If one of the conditions is not True raise an exception you define yourself: UserDoesNotExist, UserAccessExpired and UserNoPermission respectively. Check out the tests for more detail.

        Have fun and keep calm and code in Python!
    """
    try:
        secret = False #boolean flag to return SECRET

        for n in USERS:
            if n.name == username:
                #user found in tuple of users
                if n.expired == True:
                    raise UserAccessExpired
                else:
                    #user not expired
                    if n.role.lower() != 'admin':
                        raise UserNoPermission
                    else:
                         #user is an admin
                        secret = True

        if not secret:
            raise UserDoesNotExist
        else:
            return SECRET

    except UserDoesNotExist:
        print("User does not exist!")

    except UserAccessExpired:
        print("User access expired!")

    except UserNoPermission:
        print("User does not have permission!")


# def main():

    pass

# if __name__ == "__main__":
#     main()
