from functools import wraps

known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


def login_required(func):
    @wraps(func)
    def wrapper(user):
        if user not in known_users:
            return f'please create an account'
        else:
            if user in loggedin_users:
                return func(user)
            else:
                return f'please login'
    return wrapper

@login_required
def welcome(user):
    '''Return a welcome message if logged in'''
    return f'welcome back {user}'

# def main():
#     msg = welcome('anonymous')
#     print(welcome.__doc__ )


# if __name__ == "__main__":
#     main()
