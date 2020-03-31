import requests
import json


def nxapi_show_version():
    url = 'https://sbx-nxos-mgmt.cisco.com:443/ins'
    switchuser = 'admin'
    switchpassword = 'Admin_1234!'

    http_headers = {'content-type': 'application/json-rpc'}
    # payload = [{
    #     "ins_api": {
    #         "version": "1.0",
    #         "type": "cli_show",
    #         "chunk": "0",
    #         "sid": "1",
    #         "input": "show version",
    #         "output_format": "json"
    #     }
    # }]
    payload = [
        {
            "jsonrpc": "2.0",
            "method": "cli",
            "params": {
                "cmd": 'show version',
                "version": 1
            },
            "id": 1
        }]

    # print(json.dumps(payload))
    # # 1. use requests to post to the switch

    response = requests.post(url,
                             auth=(switchuser, switchpassword),
                             headers=http_headers,
                             data=json.dumps(payload),
                             verify=False)
    # print(type(response))
    # print(response.status_code)
    # print(response.text)

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

    if response.status_code == 200:
        #     # print(response.json())
        version = response.json()['result']['body']['kickstart_ver_str']

    return version


if __name__ == '__main__':
    print('please let everyone be safe...')
    result = nxapi_show_version()
    # print(type(result))
    print(result)
