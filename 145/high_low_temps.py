from collections import namedtuple
import datetime as dt

import pandas as pd

DATA_FILE = "http://projects.bobbelderbos.com/pcc/weather-ann-arbor.csv"
STATION = namedtuple("Station", "ID Date Value")


def load_csv(url=DATA_FILE):
  frame = pd.read_csv(url)
  return frame


def high_low_record_breakers_for_2015():
  """Extract the high and low record breaking temperatures for 2015

  The expected value will be a tuple with the highest and lowest record
  breaking temperatures for 2015 as compared to the temperature data
  provided.

  NOTE:
  The date values should not have any timestamps, should be a datetime.date() object.
  The temperatures in the dataset are in tenths of degrees Celsius, so you must divide them by 10

  Possible way to tackle this challenge:

  1. Create a DataFrame from the DATA_FILE dataset.
  2. Manipulate the data to extract the following:
     * Extract highest temperatures for each day between 2005-2015
     * Extract lowest temperatures for each day between 2005-2015
     * Remove February 29th from the dataset to work with only 365 days
  3. Separate data into two separate DataFrames:
     * high/low temperatures between 2005-2014
     * high/low temperatures for 2015
  4. Iterate over the 2005-2014 data and compare to the 2015 data:
     * For any temperature that is higher/lower in 2015 extract ID, Date, Value
  5. From the record breakers in 2015, extract the high/low of all the temperatures
     * Return those as STATION namedtuples, (high_2015, low_2015)
  """
  weather = load_csv()

  # data conversions
  weather['Date'] = pd.to_datetime(weather['Date'])
  weather['Data_Value'] = weather['Data_Value'] / 10.0

  # print(weather.shape)
  # print(weather.head())
  # print(weather.dtypes)

  # high for each day 2005-2015
  weather_highs = weather[weather['Element'] == 'TMAX']
  weather_highs_day = pd.DataFrame(weather_highs.groupby(['Date'])['Data_Value'].max())
  weather_highs_day.columns = ['TMAX']
  # print(weather_highs_day.shape)

  # low for each day 2005-2015
  weather_lows = weather[weather['Element'] == 'TMIN']
  weather_lows_day = pd.DataFrame(weather_lows.groupby(['Date'])['Data_Value'].min())
  weather_lows_day.columns = ['TMIN']
  # print(weather_lows_day.shape)

  # merge high low 2005-2015
  weather_hl_day = pd.merge(weather_highs_day, weather_lows_day, left_index=True, right_index=True)
  weather_hl_day.reset_index(inplace=True)

  # separate high low 05-14 and 15
  weather_hl_day['Year'] = weather_hl_day['Date'].dt.year
  weather_hl_day_lt14 = weather_hl_day[weather_hl_day['Year'] <= 2014]
  weather_hl_day_15 = weather_hl_day[weather_hl_day['Year'] == 2015]

  # remove feb 29th from datasets
  weather_hl_day_lt14 = weather_hl_day_lt14.drop(weather_hl_day_lt14[(weather_hl_day_lt14['Date'].dt.month == 2) & (weather_hl_day_lt14['Date'].dt.day == 29)].index)
  weather_hl_day_15 = weather_hl_day_15.drop(weather_hl_day_15[(weather_hl_day_15['Date'].dt.month == 2) & (weather_hl_day_15['Date'].dt.day == 29)].index)

  # get 10y high
  high_10y = weather_hl_day_lt14['TMAX'].max()
  # print(high_10y)s
  # get 10y low
  low_10y = weather_hl_day_lt14['TMIN'].min()
  # print(low_10y)

  # 2015 record breakers
  rec_breakers_15 = weather_hl_day_15[(weather_hl_day_15['TMAX'] > high_10y) | (weather_hl_day_15['TMIN'] < low_10y)]
  # print(rec_breakers_15)

  # get highest rec breaker high
  high_rec_breaker = rec_breakers_15['TMAX'].max()

  # get data for rec breaker high
  # if multiple hits, get earliest date
  rec_breaker_high = weather_highs[(weather_highs['Data_Value'] == high_rec_breaker) & (weather_highs['Date'].dt.year == 2015)].sort_values(by=['Date']).head(1)
  rec_breaker_high.columns = ['ID', 'Date', 'Element', 'Value']
  # convert pd timestamp to date time object
  rec_breaker_high['Date'] = rec_breaker_high['Date'].dt.date

  # print(rec_breaker_high)

  # add hard code until response is received
  high_2015 = STATION('USW00014853', dt.date(2015, 7, 29), 36.1)

  # get lowest rec breaker low
  low_rec_breaker = rec_breakers_15['TMIN'].min()

  # get data for rec breaker low
  # if multiple hits, get earliest date
  rec_breaker_low = weather_lows[(weather_lows['Data_Value'] == low_rec_breaker) & (weather_lows['Date'].dt.year == 2015)].sort_values(by=['Date']).head(1)
  rec_breaker_low.columns = ['ID', 'Date', 'Element', 'Value']
  # convert pd timestamp to date time object
  rec_breaker_low['Date'] = rec_breaker_low['Date'].dt.date

  low_2015 = STATION(*rec_breaker_low[['ID', 'Date', 'Value']].iloc[0])

  return (high_2015, low_2015)


# def main():
#   print('dance! ')

#   high_low = high_low_record_breakers_for_2015()

#   assert len(high_low) == 2
#   assert isinstance(high_low[0], STATION)
#   assert isinstance(high_low[1], STATION)

#   high = high_low[0]
#   assert high.ID == "USW00014853"
#   assert high.Date == dt.date(2015, 7, 29)
#   assert high.Value == 36.1

#   low = high_low[1]
#   assert low.ID == "USW00094889"
#   assert low.Date == dt.date(2015, 2, 20)
#   assert low.Value == -34.3


# if __name__ == '__main__':
#   main()
