from pathlib import Path
import csv
import json
from json.decoder import JSONDecodeError
import os
from urllib.request import urlretrieve


EXCEPTION = 'exception caught'

local = os.getcwd()

mount1_expected = [
    ['creatureId', 'icon', 'isAquatic', 'isFlying', 'isGround', 'isJumping',
     'itemId', 'name', 'qualityId', 'spellId'],
    ['32158', 'ability_mount_drake_blue', 'False', 'True', 'True', 'False',
     '44178', 'Albino Drake', '4', '60025'],
    ['63502', 'ability_mount_hordescorpionamber', 'True', 'False', 'True',
     'True', '85262', 'Amber Scorpion', '4', '123886'],
    ['24487', 'ability_mount_warhippogryph', 'False', 'True', 'True', 'False',
     '45725', 'Argent Hippogryph', '4', '232412'],
]

mount2_expected = [
    ['creatureId', 'icon', 'isAquatic', 'isFlying', 'isGround', 'isJumping',
     'itemId', 'name', 'qualityId', 'spellId'],
    ['71381', 'ability_mount_dragonhawkarmorallliance', 'False', 'True',
     'True', 'False', '98259', 'Armored Blue Dragonhawk', '4', '142478'],
    ['304', 'spell_nature_swiftness', 'True', 'False', 'True', 'True', '0',
     'Felsteed', '1', '5784'],
    ['119386', 'inv_warlockmount', 'False', 'True', 'True', 'False', '0',
     "Netherlord's Chaotic Wrathsteed", '1', '232412'],
]


mount_data = (
    'https://bites-data.s3.us-east-2.amazonaws.com/'
    'mount-data{}.json'
)
file_no = 3
TMP = Path('/tmp')
# TMP = Path(local)
mount_json = TMP / f'mount{file_no}.json'
urlretrieve(mount_data.format(file_no), mount_json)


def convert_to_csv(json_file: str):
  """Read/load the json_file (local file downloaded to /tmp) and
     convert/write it to defined csv_file.
      The data is in mounts > collected

     Catch bad JSON (JSONDecodeError) file content, in that case print the defined
     EXCEPTION string ('exception caught') to stdout reraising the exception.
     This is to make sure you actually caught this exception.

     Example csv output:
     creatureId,icon,isAquatic,isFlying,isGround,isJumping,itemId,name,qualityId,spellId
     32158,ability_mount_drake_blue,False,True,True,False,44178,Albino Drake,4,60025
     63502,ability_mount_hordescorpionamber,True,...
     ...
  """  # noqa E501
  csv_file = TMP / json_file.name.replace('.json', '.csv')
  # you code

  try:
    with open(str(json_file), 'r') as j:
      d = json.load(j)
    # json_parsed = json.loads(f)

    collected = d['mounts']['collected']

    csv_data = open(csv_file, 'w')
    csvwriter = csv.writer(csv_data)
    count = 0

    for c in collected:
      if count == 0:
        header = c.keys()
        csvwriter.writerow(header)

      count += 1
      csvwriter.writerow(c.values())

    # csv_data.close()

    return csv_file

  except JSONDecodeError as jex:
    print(EXCEPTION)
    raise jex


# def main():
#   print('thank you for everything...')
#   csv_file = convert_to_csv(mount_json)
#   # print(type(convert_to_csv(mount_json)['mounts']['collected'][0]))
#   if csv_file:
#     with open(csv_file) as csv_file:
#       actual = list(csv.reader(csv_file))
#       assert actual == mount2_expected


# if __name__ == '__main__':
#   main()
