import hashlib

GRAVATAR_URL = ("https://www.gravatar.com/avatar/"
                "{hashed_email}?s={size}&r=g&d=robohash")


def create_gravatar_url(email, size=200):
    """Use GRAVATAR_URL above to create a gravatar URL.

       You need to create a hash of the email passed in.

       PHP example: https://en.gravatar.com/site/implement/hash/

       For Python check hashlib check out (md5 / hexdigest):
       https://docs.python.org/3/library/hashlib.html#hashlib.hash.hexdigest
    """
    hash_object = hashlib.md5(email.replace(' ', '').strip().lower().encode())
    hex_eq = hash_object.hexdigest()

    return GRAVATAR_URL.format(hashed_email=hex_eq, size=size)


# def main():

#     print('paddle to the buoy... and then waves!')
#     what = create_gravatar_url(' support@pybit.es', 1000)
#     print(what)


# if __name__ == '__main__':
#     main()
