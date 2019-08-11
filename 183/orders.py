from os import path
from urllib.request import urlretrieve
import os

import pandas as pd
from pandas.core.frame import DataFrame

# local = os.getcwd()
local = '/tmp'

EXCEL = path.join(local, 'order_data.xlsx')
if not path.isfile(EXCEL):
  urlretrieve('https://bit.ly/2JpniQ2', EXCEL)


def load_excel_into_dataframe(excel=EXCEL):
  """Load the SalesOrders sheet of the excel book (EXCEL variable)
     into a Pandas DataFrame and return it to the caller"""

  sales_df = pd.read_excel(excel, 'SalesOrders')

  return sales_df


def get_year_region_breakdown(df):
  """Group the DataFrame by year and region, summing the Total
     column. You probably need to make an extra column for
     year, return the new df as shown in the Bite description
  """
  df_deep = df.copy()
  df_deep['Year'] = df_deep['OrderDate'].dt.year
  grouped = df_deep.groupby(['Year', 'Region'])['Total'].agg('sum')
  return grouped


def get_best_sales_rep(df):
  """Return a tuple of the name of the sales rep and
     the total of his/her sales"""
  df_deep = df.copy()
  # df_deep['Year'] = df_deep['OrderDate'].dt.year
  best_rep = df_deep.groupby(['Rep'])['Total'].agg('sum').sort_values(ascending=False).head(1)

  return tuple(zip(best_rep.index, best_rep))[0]


def get_most_sold_item(df):
  """Return a tuple of the name of the most sold item
     and the number of units sold"""
  df_deep = df.copy()
  most_sold = df_deep.groupby(['Item'])['Units'].agg('sum').sort_values(ascending=False).head(1)

  return tuple(zip(most_sold.index, most_sold))[0]


# def main():
#   """
#       OrderDate   Region      Rep    Item  Units  Unit Cost   Total
#     0 2018-01-06     East    Jones  Pencil     95       1.99  189.05
#     1 2018-01-23  Central   Kivell  Binder     50      19.99  999.50
#     2 2018-02-09  Central  Jardine  Pencil     36       4.99  179.64
#     3 2018-02-26  Central     Gill     Pen     27      19.99  539.73
#     4 2018-03-15     West  Sorvino  Pencil     56       2.99  167.44
#   """
#   frame = load_excel_into_dataframe()
#   assert type(frame) == DataFrame
#   assert frame.shape == (43, 7)

#   # print(frame.describe(include='all'))
#   # print(frame.dtypes)
#   ret = get_year_region_breakdown(frame)
#   # print(ret)
#   # print(frame.head())
#   assert ret.index.levels[0][0] == 2018
#   assert ret.index.levels[0][1] == 2019
#   assert ret.index.names[0] == 'Year'
#   assert ret.index.names[1] == 'Region'

#   best_rep = get_best_sales_rep(frame)
#   # print(best_rep)
#   # print(type(best_rep))
#   assert best_rep[0] == 'Kivell'
#   assert best_rep[1] == 3109.44

#   most_sold = get_most_sold_item(frame)
#   # print(most_sold)
#   assert most_sold[0] == 'Binder'
#   assert int(most_sold[1]) == 722


# if __name__ == "__main__":
#   main()
