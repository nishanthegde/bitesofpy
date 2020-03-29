import requests


def nxapi_show_version():
    url = """ please fill in """
    switchuser = 'admin'
    switchpassword = 'Admin_1234!'

    url='http://<IP_Address>/ins'
    switchuser='<User_ID>'
    switchpassword='<Password>'


    http_headers = {""" please fill in """}
    payload = [{"jsonrpc": "2.0",
                "method": 'cli',
                "params": {"cmd": 'cli_show',
                           "version": 1}, "id": 1}]
    # 1. use requests to post to the switch
    response = ...
    print(type(response))
    print(response)

    # 2. retrieve and return the kickstart_ver_str from the response
    # example response json:
    # {'result': {'body': {'bios_cmpl_time': '05/17/2018',
    #                      'kick_tmstmp': '07/11/2018 00:01:44',
    #                      'kickstart_ver_str': '9.2(1)',
    #                      ...
    #                      }
    #             }
    # }
    version = ...
    return version


if __name__ == '__main__':
    print('please let everyone be safe...')
    result = nxapi_show_version()
    print(type(result))
    print(result)
