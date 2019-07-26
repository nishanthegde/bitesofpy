import requests

STOCK_DATA = 'https://bit.ly/2MzKAQg'

#load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float

      helper function to format cap
    """

    if 'n/a' in cap:
      return 0

    if 'M'.lower() in cap.lower():
      return float(cap.lower().replace('m','').replace('$',''))

    if 'B'.lower() in cap.lower():
      return float(cap.lower().replace('b','').replace('$',''))*1000

    return None


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision
    """
    return round(sum([_cap_str_to_mln_float(d['cap']) for d in data if d['industry'].lower() == industry.lower()]),2)



def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    mx_cap = max([_cap_str_to_mln_float(d['cap']) for d in data])

    return [d['symbol'] for d in data if _cap_str_to_mln_float(d['cap']) == mx_cap][0]

def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    # d = {x['sector']:data.count(x['symbol']) for x in data}
    count_stocks = {}
    no_na = [d for d in data if d['sector'] != 'n/a']

    for d in no_na:
      if d['sector'] not in count_stocks:
        count_stocks[d['sector']] = 1
      else:
        count_stocks[d['sector']] += 1

    return (max(count_stocks, key=count_stocks.get), min(count_stocks, key=count_stocks.get))

# def main():

#     # print(type(data))
#     # print(len(data))
#     # print(data[:1])

#     # assert _cap_str_to_mln_float('n/a') == 0
#     # assert _cap_str_to_mln_float('$100.45M') == 100.45
#     # assert _cap_str_to_mln_float('$20.9B') == 209001

#     # print(len([_cap_str_to_mln_float(d['cap']) for d in data]))
#     # print(get_industry_cap('Business Services'))
#     # print(get_industry_cap('Real Estate Investment Trusts'))
#     # assert get_stock_symbol_with_highest_cap() == 'JNJ'

#     # i = ['apple','red','apple','red','red','pear']
#     # d = {x:i.count(x) for x in i}
#     what = get_sectors_with_max_and_min_stocks()
#     print(what)

# if __name__ == "__main__":
#   main()
