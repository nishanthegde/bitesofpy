data = """Luke Skywalker,172,77
          C-3PO,167,75
          R2-D2,96,32
          Darth Vader,202,136
          Leia Organa,150,49
          Owen Lars,178,120
          Beru Whitesun lars,165,75
          R5-D4,97,32
          Biggs Darklighter,183,84
          Obi-Wan Kenobi,182,77
          Anakin Skywalker,188,84
          Chewbacca,228,112
          Han Solo,180,80
          Greedo,173,74
          Jek Tono Porkins,180,110
          Yoda,66,17
          Palpatine,170,75
          Boba Fett,183,78.2
          IG-88,200,140
          Bossk,190,113
"""


def person_max_bmi(data: str=data) -> tuple:
  """Return (name, BMI float) of the character in data that
     has the highest BMI (rounded on 2 decimals)"""
  characters = [tuple(c.strip().split(',')) for c in data.splitlines()]

  bmis = [(t[0], round(float(t[2]) / ((int(t[1]) / 100) ** 2), 2)) for t in characters]

  # print(bmis)
  return sorted(bmis, key=lambda x: x[1], reverse=True)[0]


# def main():
#   print('thank you for everything... ')
#   print(person_max_bmi())
#   assert person_max_bmi() == ('Yoda', 39.03)

#   newdata = '\n'.join(data.splitlines()[:10])
#   newdata = '\n'.join([row for row in data.splitlines()
#                        if row.lstrip()[:4] not in ('Owen', 'Yoda')])
#   print(newdata)
#   # assert person_max_bmi(newdata) == ('Owen Lars', 37.87)
#   assert person_max_bmi(newdata) == ('IG-88', 35.0)


# if __name__ == '__main__':
#   main()
