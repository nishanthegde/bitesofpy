from pathlib import Path
from urllib.request import urlretrieve

from bs4 import BeautifulSoup as Soup

import os
import re

mock_html = """
<table id="minecraft_items" class="std_table">
<tr>
<th data-search="1" width="175">Enchantment<br>(<em>Minecraft ID Name</em>)</th>
<th data-search="1">Max Level</th>
<th class="hidden-xs">Description</th>
<th data-search="1"><span class="hidden-xs">Minecraft </span>ID</th>
<th class="hidden-xs">Items</th>
<th>Version</th>
</tr>
<tr>
<td><a href="/enchantments/aqua_affinity.php">Aqua Affinity</a><br>(<em>aqua_<wbr>affinity</em>)</td>
<td>I</td>
<td class="hidden-xs">Speeds up how fast you can mine blocks underwater</td>
<td>6</td>
<td class="hidden-xs"><img class="img-rounded b-lazy" src="/images/thumbnail_loading.gif" data-src="/armor_recipes/images/enchanted_iron_helmet.png" alt="aqua affinity" width="40" height="40"></td>
<td></td>
</tr>
<tr>
<td><a href="/enchantments/bane_of_arthropods.php">Bane of Arthropods</a><br>(<em>bane_<wbr>of_<wbr>arthropods</em>)</td>
<td>V</td>
<td class="hidden-xs">Increases attack damage against arthropods</td>
<td>18</td>
<td class="hidden-xs"><img class="img-rounded b-lazy" src="/images/thumbnail_loading.gif" data-src="/enchantments/images/sword_axe_sm.png" alt="bane of arthropods" width="40" height="40"></td>
<td></td>
</tr>
<tr>
<td><a href="/enchantments/blast_protection.php">Blast Protection</a><br>(<em>blast_<wbr>protection</em>)</td>
<td>IV</td>
<td class="hidden-xs">Reduces blast and explosion damage</td>
<td>3</td>
<td class="hidden-xs"><img class="img-rounded b-lazy" src="/images/thumbnail_loading.gif" data-src="/enchantments/images/armor_sm.png" alt="blast protection" width="40" height="40"></td>
<td></td>
</tr>
<tr>
<td><a href="/enchantments/channeling.php">Channeling</a><br>(<em>channeling</em>)</td>
<td>I</td>
<td class="hidden-xs">Summons a lightning bolt at a targeted mob when enchanted item is thrown (targeted mob must be standing in raining)</td>
<td>68</td>
<td class="hidden-xs"><img class="img-rounded b-lazy" src="/images/thumbnail_loading.gif" data-src="/weapon_recipes/images/enchanted_trident.png" alt="channeling" width="40" height="40"></td>
<td>1.13</td>
</tr>
</table>
"""

out_dir = os.getcwd()
out_dir = "/tmp"
html_file = f"{out_dir}/enchantment_list_pc.html"

HTML_FILE = Path(html_file)
URL = "https://www.digminecraft.com/lists/enchantment_list_pc.php"


class Enchantment:
  """Minecraft enchantment class

  Implements the following:
      id_name, name, max_level, description, items
  """

  def __init__(self, id_name, name, max_level, description, items=[]):

    self.id_name = id_name
    self.name = name
    self.max_level = max_level
    self.description = description
    self.items = items

  def __str__(self):
    return "{} ({}): {}".format(self.name, self.max_level, self.description)


class Item:
  """Minecraft enchantable item class

  Implements the following:
      name, enchantments
  """

  def __init__(self, name, enchantments=[]):

    self.name = name
    self.enchantments = enchantments

  def __str__(self):
    str1 = "{}: \n".format(self.name.replace('_', ' ').title())

    str2 = ''
    self.enchantments.sort(key=lambda x: x.id_name)
    for e in self.enchantments:
      str2 += "  [{}] {}\n".format(e.max_level, e.id_name)

    return str1 + str2.rstrip('\n')


def generate_enchantments(soup):
  """Generates a dictionary of Enchantment objects

  With the key being the id_name of the enchantment.
  """

  enchantments = {}

  name_regex = re.compile(r'^([^(]*)\((.*)\)')

  replace_dict = {'.': '', 'enchanted': '', 'iron': '', 'png': '', 'sm': ''}

  # parse enchantments from table
  table = soup.find('table', {'id': 'minecraft_items'})
  rows = table.find_all('tr')

  for row in rows:
    cols = row.find_all('td')
    if cols:
      # print(cols)
      name = name_regex.search(cols[0].text).group(1)
      id_name = name_regex.search(cols[0].text).group(2)
      max_level = int(_roman_to_int(cols[1].text))
      description = cols[2].text
      for img in cols[4].find_all('img'):
        # get image file name
        img_file = img.get('data-src').rsplit('/', 1)[1]
        # clean and then strip leading and trailing _ (retain _ in the middle)
        img_file = replace_all(img_file, replace_dict).strip('_')
        # keep fishing_rod
        img_file = img_file.replace('fishing_rod', 'fishing**rod')
        items = [i.replace('**', '_') for i in img_file.split('_')]
        # print(items)

      # create instances of enchanments
      # if id_name == 'vanishing_curse' or id_name == 'unbreaking' or id_name == 'protection':
      #   enchantments[id_name] = Enchantment(id_name, name, max_level, description, items)

      enchantments[id_name] = Enchantment(id_name, name, max_level, description, items)

  return enchantments  # dict(sorted(enchantments.items()))


def generate_items(data):
  """Generates a dictionary of Item objects

  With the key being the item name.
  """

  items = {}

  for e in data:  # for each enchantment vanishing_curse
    # j = 0
    for i in data[e].items:  # for each item in the item list of the enchantment
      #['sword', 'chestplate', 'pickaxe', 'fishing_rod']
      if i not in items:  # not in dict
        i = Item(i, [data[e]])
        items[i.name] = i  # create Item object
      else:  # in dict
        items[i].enchantments.append(data[e])

  # for i in items:
  #   # for e in items[i].enchantments:
  #   #   print(e.id_name)
  #   items[i].enchantments.sort(key=lambda x: x.id_name)

  return dict(sorted(items.items()))


def get_soup(file=HTML_FILE):
  """Retrieves/takes source HTML and returns a BeautifulSoup object"""
  if isinstance(file, Path):
    if not HTML_FILE.is_file():
      urlretrieve(URL, HTML_FILE)

    with file.open() as html_source:
      soup = Soup(html_source, "html.parser")
  else:
    soup = Soup(file, "html.parser")

  return soup


def replace_all(text, d):

  for k, v in d.items():
    text = text.replace(k, v)

  return text


def enchantment_mock():
  enchant = Enchantment(
      "python_developer",
      "Python Developer",
      10,
      "Ability automate really boring and repetitive tasks at work",
  )
  return enchant


def item_mock():
  item = Item("clamytoe")
  return item


def value(r):
  if (r == 'I'):
    return 1
  if (r == 'V'):
    return 5
  if (r == 'X'):
    return 10
  if (r == 'L'):
    return 50
  if (r == 'C'):
    return 100
  if (r == 'D'):
    return 500
  if (r == 'M'):
    return 1000
  return -1


def _roman_to_int(str):
  res = 0
  i = 0

  while (i < len(str)):

    # Getting value of symbol s[i]
    s1 = value(str[i])

    if (i + 1 < len(str)):

      # Getting value of symbol s[i+1]
      s2 = value(str[i + 1])

      # Comparing both values
      if (s1 >= s2):

        # Value of current symbol is greater
        # or equal to the next symbol
        res = res + s1
        i = i + 1
      else:

        # Value of current symbol is greater
        # or equal to the next symbol
        res = res + s2 - s1
        i = i + 2
    else:
      res = res + s1
      i = i + 1

  return res


def main():
  """This function is here to help you test your final code.

  Once complete, the print out should match what's at the bottom of this file"""
  soup = get_soup()
  enchantment_data = generate_enchantments(soup)
  # print(enchantment_data)
  minecraft_items = generate_items(enchantment_data)

  for item in minecraft_items:
    print(minecraft_items[item], "\n")

  """
  # validate test file below this
  assert enchantment_mock().name == "Python Developer"
  assert enchantment_mock().items == []
  # print(enchantment_mock().id_name)
  # print(enchantment_mock().max_level)
  # enchantment_mock().items.append(item_mock().name)
  # assert len(enchantment_mock().items) == 1
  # bob = Item("bob")
  # enchantment_mock().items.append(bob.name)
  # assert len(enchantment_mock().items) == 2
  # assert enchantment_mock().items == ["clamytoe", "bob"]
  # assert enchantment_mock().max_level == 10
  test = enchantment_mock()
  # print(test)
  op = "Python Developer (10): Ability automate really boring and repetitive tasks at work"
  # print(op)
  assert str(test) == op

  item_mock().enchantments.append(enchantment_mock())
  # item_mock().enchantments.append(enchantment_mock())
  # assert item_mock().enchantments[0].name == "Python Developer"

  test = item_mock()
  # print(test)
  output = "Clamytoe: \n  [10] python_developer"
  # print(output)
  assert str(test) == output

  soup = get_soup(mock_html)
  enchantment_data = generate_enchantments(soup)
  test = enchantment_data['channeling']
  # print(test)
  output = "Channeling (1): Summons a lightning bolt at a targeted mob when enchanted item is thrown (targeted mob must be standing in raining)"
  # print(output)
  assert str(test) == output

  test = enchantment_data['aqua_affinity']
  # print(test.max_level)

  test = enchantment_data['bane_of_arthropods']
  # print(test.max_level)

  test = enchantment_data['blast_protection']
  # print(test.max_level)

  test = enchantment_data['channeling']
  # print(test.max_level)

  assert isinstance(enchantment_data, dict)
  assert len(enchantment_data.keys()) == 4

  # test = enchantment_data["channeling"].description
  # op = "Summons a lightning bolt at a targeted mob when enchanted item is thrown (targeted mob must be standing in raining)"

  # assert test == op

  # soup = get_soup()
  # data = generate_enchantments(soup)

  # assert len(data.keys()) == 37
  # assert data["efficiency"].max_level == 5

  test = generate_items(enchantment_data)["armor"].enchantments[0].name
  # print(test)

  test = generate_items(enchantment_data)["axe"].enchantments[0].name
  # print(test)

  test = generate_items(enchantment_data)["helmet"].enchantments[0].name
  # print(test)

  test = generate_items(enchantment_data)["sword"].enchantments[0].name
  # print(test)

  test = generate_items(enchantment_data)["trident"].enchantments[0].name
  # print(test)

  soup = get_soup()
  mc_data = generate_enchantments(soup)
  items = generate_items(mc_data)

  # print(items)

  print([enc.id_name for enc in items["armor"].enchantments])

  print(items["armor"])
"""


if __name__ == "__main__":
  main()

"""
Armor:
  [1] binding_curse
  [4] blast_protection
  [4] fire_protection
  [4] projectile_protection
  [4] protection
  [3] thorns

Axe:
  [5] bane_of_arthropods
  [5] efficiency
  [3] fortune
  [5] sharpness
  [1] silk_touch
  [5] smite

Boots:
  [3] depth_strider
  [4] feather_falling
  [2] frost_walker

Bow:
  [1] flame
  [1] infinity
  [5] power
  [2] punch

Chestplate:
  [1] mending
  [3] unbreaking
  [1] vanishing_curse

Crossbow:
  [1] multishot
  [4] piercing
  [3] quick_charge

Fishing Rod:
  [3] luck_of_the_sea
  [3] lure
  [1] mending
  [3] unbreaking
  [1] vanishing_curse

Helmet:
  [1] aqua_affinity
  [3] respiration

Pickaxe:
  [5] efficiency
  [3] fortune
  [1] mending
  [1] silk_touch
  [3] unbreaking
  [1] vanishing_curse

Shovel:
  [5] efficiency
  [3] fortune
  [1] silk_touch

Sword:
  [5] bane_of_arthropods
  [2] fire_aspect
  [2] knockback
  [3] looting
  [1] mending
  [5] sharpness
  [5] smite
  [3] sweeping
  [3] unbreaking
  [1] vanishing_curse

Trident:
  [1] channeling
  [5] impaling
  [3] loyalty
  [3] riptide
"""
