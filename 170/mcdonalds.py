import pandas as pd

data = "https://s3.us-east-2.amazonaws.com/bites-data/menu.csv"
# load the data in once, functions will use this module object
df = pd.read_csv(data)

pd.options.mode.chained_assignment = None  # ignore warnings


def get_food_most_calories(df=df):
  """Return the food "Item" string with most calories"""
  highest_calories = df.groupby(['Item'])['Calories'].agg('sum').sort_values(ascending=False).head(1)
  return list(highest_calories.index)[0]


def get_bodybuilder_friendly_foods(df=df, excl_drinks=False):
  """Calulate the Protein/Calories ratio of foods and return the
     5 foods with the best ratio.

     This function has a excl_drinks switch which, when turned on,
     should exclude 'Coffee & Tea' and 'Beverages' from this top 5.

     You will probably need to filter out foods with 0 calories to get the
     right results.

     Return a list of the top 5 foot Item stings."""

  # remove 0 cal foods
  df = df[df['Calories'] > 0]

  df = df.groupby(['Category', 'Item']).agg({'Protein': 'sum', 'Calories': 'sum'}).reset_index()

  df['Protein Per Calorie'] = df['Protein'] / df['Calories']

  if excl_drinks:
    df = df[(df['Category'] != 'Coffee & Tea') & (df['Category'] != 'Beverages')]

  df = df.sort_values(by=['Protein Per Calorie'], ascending=False)

  return df['Item'].head(5)


# def main():

#   # print('dance')

#   actual = get_food_most_calories()
#   expected = 'Chicken McNuggets (40 piece)'
#   assert actual == expected

#   df_breakfast = df[df['Category'] == 'Breakfast']
#   actual = get_food_most_calories(df_breakfast)
#   expected = 'Big Breakfast with Hotcakes (Large Biscuit)'
#   assert actual == expected

#   # get_bodybuilder_friendly_foods()

#   actual_with_drinks = list(get_bodybuilder_friendly_foods())
#   # print(actual_with_drinks)
#   expected = ['Premium Bacon Ranch Salad with Grilled Chicken',
#               'Nonfat Latte (Small)',
#               'Nonfat Latte (Large)',
#               'Premium Southwest Salad with Grilled Chicken',
#               'Nonfat Latte (Medium)']

#   assert all(food in actual_with_drinks for food in expected)

#   actual_wo_drinks = list(get_bodybuilder_friendly_foods(excl_drinks=True))

#   expected = ['Premium Bacon Ranch Salad with Grilled Chicken',
#               'Premium Southwest Salad with Grilled Chicken',
#               'Premium Grilled Chicken Classic Sandwich',
#               'Premium Grilled Chicken Ranch BLT Sandwich',
#               'Premium Grilled Chicken Club Sandwich']

#   assert all(food in actual_wo_drinks for food in expected)


# if __name__ == '__main__':
#   main()
