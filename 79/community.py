import csv
import requests
# from collections import Counter

CSV_URL = 'https://bit.ly/2HiD2i8'

def get_csv():
    """Use requests to download the csv and return the
       decoded content"""

    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')

        cr = csv.reader(decoded_content.splitlines(), delimiter=',')

        return list(cr)

def create_user_bar_chart(content):
    """Receives csv file (decoded) content and returns a table of timezones
       and their corresponding member counts in pluses (see Bite/tests)"""
    all_tz = sorted([x[2] for x in content[1:]])
    tz_counts = dict((x,all_tz.count(x)) for x in set(all_tz))
    longest_key = max([len(k) for k in tz_counts.keys()])
    # print(longest_key)

    for key in sorted(tz_counts.keys()):
        bars = '+'*tz_counts[key]
        pad =  ' '*(longest_key + 1 - len(key))
        print(f'{key}'+ pad + ' | ' + bars)


# def main():
#     content = get_csv()
#     create_user_bar_chart(content)

# if __name__ == "__main__":
#     main()
