import requests

IPINFO_URL = 'http://ipinfo.io/{ip}/json'


def get_ip_country(ip_address: str) -> str:
    """Receives ip address string, use IPINFO_URL to get geo data,
       parse the json response returning the country code of the IP"""
    resp = requests.get(IPINFO_URL.format(ip=ip_address))

    return eval(resp.text)['country']


# def main():
#     print('...thanks...')
#     print(get_ip_country('187.190.38.36'))
#     print(get_ip_country('185.161.200.10'))


# if __name__ == '__main__':
#     main()
