import test_users as t
import re


def get_users(passwd: str) -> dict:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    users = dict()

    pattern = re.compile(r'\s{2,}')


    for l in passwd.strip().splitlines():
        if l.split(':')[4]:
            users[l.split(':')[0]] = re.sub(pattern, ' ', l.split(':')[4].replace(',', ' ').strip())
        else:
            users[l.split(':')[0]] = 'unknown'
        # print(l.split(':'))

    return users


def main():
    print('thank you for everything...')
    print(get_users(t.pw4))


if __name__ == '__main__':
    main()
