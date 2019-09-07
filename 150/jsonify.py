import json

members = """
id,first_name,last_name,email
1,Junie,Kybert;jkybert0@army.mil
2,Sid,Churching|schurching1@tumblr.com
3,Cherry;Dudbridge,cdudbridge2@nifty.com
4,Merrilee,Kleiser;mkleiser3@reference.com
5,Umeko,Cray;ucray4@foxnews.com
6,Jenifer,Dale|jdale@hubpages.com
7,Deeanne;Gabbett,dgabbett6@ucoz.com
8,Hymie,Valentin;hvalentin7@blogs.com
9,Alphonso,Berwick|aberwick8@symantec.com
10,Wyn;Serginson,wserginson9@naver.com
"""

# test = [{'id': '1', 'first_name': 'Junie', 'last_name': 'Kybert',
#          'email': 'jkybert0@army.mil'},
#         {'id': '2', 'first_name': 'Sid', 'last_name': 'Churching',
#          'email': 'schurching1@tumblr.com'},
#         {'id': '3', 'first_name': 'Cherry', 'last_name': 'Dudbridge',
#          'email': 'cdudbridge2@nifty.com'},
#         {'id': '4', 'first_name': 'Merrilee', 'last_name': 'Kleiser',
#          'email': 'mkleiser3@reference.com'},
#         {'id': '5', 'first_name': 'Umeko', 'last_name': 'Cray',
#          'email': 'ucray4@foxnews.com'},
#         {'id': '6', 'first_name': 'Jenifer',
#          'last_name': 'Dale', 'email': 'jdale@hubpages.com'},
#         {'id': '7', 'first_name': 'Deeanne', 'last_name': 'Gabbett',
#          'email': 'dgabbett6@ucoz.com'},
#         {'id': '8', 'first_name': 'Hymie', 'last_name': 'Valentin',
#          'email': 'hvalentin7@blogs.com'},
#         {'id': '9', 'first_name': 'Alphonso', 'last_name':
#          'Berwick', 'email': 'aberwick8@symantec.com'},
#         {'id': '10', 'first_name': 'Wyn', 'last_name': 'Serginson',
#          'email': 'wserginson9@naver.com'}]


def convert_to_json(members=members):

    output = []

    members_cleaned = [m.replace(';', ',').replace('|', ',') for m in members.splitlines() if m]

    keys = members_cleaned[0].split(',')

    for member in members_cleaned[1:]:
        values = member.split(',')
        output.append(dict(zip(keys, values)))

    return json.dumps(output)


# def main():
#     output = convert_to_json()
#     print(output)
#     assert type(output) == str
#     assert len(output) == 938
#     # s = ''
#     # for t in test:
#     #     s += str(t) + ' \n'
#     # print(type(s))
#     # print(len(s))
#     # output = json.dumps(test)
#     # print(type(output))
#     # print(len(output))
#     data = json.loads(output)

#     for row in [{'id': '1', 'first_name': 'Junie', 'last_name': 'Kybert',
#                  'email': 'jkybert0@army.mil'},
#                 {'id': '2', 'first_name': 'Sid', 'last_name': 'Churching',
#                  'email': 'schurching1@tumblr.com'},
#                 {'id': '3', 'first_name': 'Cherry', 'last_name': 'Dudbridge',
#                  'email': 'cdudbridge2@nifty.com'},
#                 {'id': '4', 'first_name': 'Merrilee', 'last_name': 'Kleiser',
#                  'email': 'mkleiser3@reference.com'},
#                 {'id': '5', 'first_name': 'Umeko', 'last_name': 'Cray',
#                  'email': 'ucray4@foxnews.com'},
#                 {'id': '6', 'first_name': 'Jenifer',
#                  'last_name': 'Dale', 'email': 'jdale@hubpages.com'},
#                 {'id': '7', 'first_name': 'Deeanne', 'last_name': 'Gabbett',
#                  'email': 'dgabbett6@ucoz.com'},
#                 {'id': '8', 'first_name': 'Hymie', 'last_name': 'Valentin',
#                  'email': 'hvalentin7@blogs.com'},
#                 {'id': '9', 'first_name': 'Alphonso', 'last_name':
#                  'Berwick', 'email': 'aberwick8@symantec.com'},
#                 {'id': '10', 'first_name': 'Wyn', 'last_name': 'Serginson',
#                  'email': 'wserginson9@naver.com'}]:
#         assert row in data


# if __name__ == '__main__':
#     main()
