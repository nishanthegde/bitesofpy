# version might be fictitious for testing purposes
old_reqs = """
certifi==2017.4.17
chardet==3.0.4
click==6.7
Faker==0.7.12
Flask==0.12.1
"""
new_reqs = """
certifi==2016.11.29
chardet==2.0.4
click==5.0
Faker==1.0.2
Flask==1.0.2
"""

other_old_reqs = """
twilio==6.23.1
urllib3==1.21.1
Werkzeug==0.12.1
WTForms==1.19.0
"""
other_new_reqs = """
twilio==6.3.0
urllib3==1.21.1
Werkzeug==0.14.1
WTForms==2.1
"""


def changed_dependencies(old_reqs: str, new_reqs: str) -> list:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    old = old_reqs.strip().splitlines()
    new = new_reqs.strip().splitlines()

    upgraded = []

    for o, n in list(zip(old, new)):
        o_pkg = o.split('==')[0]
        o_ver = o.split('==')[1].split('.')
        o_ver = [int(v) for v in o_ver]

        n_pkg = n.split('==')[0]
        n_ver = n.split('==')[1].split('.')
        n_ver = [int(v) for v in n_ver]

        checks = min(len(o_ver), len(n_ver))
        proceed = True
        for i in range(0, checks):
            if n_ver[i] < o_ver[i]:
                proceed = False
            if proceed and n_ver[i] > o_ver[i] and o_pkg == n_pkg:
                upgraded.append(o_pkg)

        # for i in range(0, len(o_ver)):
        #     if n_ver[i] < o_ver[i]

        # print(o_ver, n_ver)
    return upgraded


# def main():
#     print('thank you for the curiosity ...')
#     print(changed_dependencies(old_reqs, new_reqs))
#     print(changed_dependencies(other_old_reqs, other_new_reqs))


# if __name__ == '__main__':
#     main()
