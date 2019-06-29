import string
import re

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())

def validate_password(password):
    """
        validates password for
        is between 6 and 12 chars long (both inclusive)
        has at least 1 digit [0-9]
        has at least two lowercase chars [a-z]
        has at least one uppercase char [A-Z]
        has at least one punctuation char (use: PUNCTUATION_CHARS)
        has not been used before (use: used_passwords)

        if the password matches all criteria the function stores the password in used_passwords and returns True
    """
    valid = False

    if len(password) < 6 or len(password) > 12:
        print("pwd length must be between 6 and 12 chars long")
    else:
        if not bool(re.search(r'\d+', password)):
            print("pwd must contain at least 1 digit")
        else:
            if not re.search(r'^(?=(.*[a-z]){2})', password):
                print("pwd must contain at least 2 lowercase chars")
            else:
                if not re.search(r'^(?=.*[A-Z])', password):
                    print("pwd must contain at least 1 uppercase char")
                else:
                    if not [password.find(p) for p in PUNCTUATION_CHARS if password.find(p) >=0]: # no pucntuation characters found = empty list
                        print("pwd must contain at least one punctuation char")
                    else:
                        if password in used_passwords:
                            print("pwd must not have been used before")
                        else:
                            used_passwords.add(password)
                            print("here")
                            valid = True

    return valid

# def main():

#     print(used_passwords)
#     validate_password('go1@PW')
#     print(used_passwords)
#     validate_password('PyBites@1912')
#     print(used_passwords)
#     validate_password('PyBites@1912')

# if __name__ == "__main__":
#     main()
