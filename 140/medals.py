import pandas as pd

data = "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"


def athletes_most_medals(data=data) -> dict:
    frame = pd.read_csv(data)

    frame_men = frame[frame['Gender'] == 'Men']
    frame_women = frame[frame['Gender'] == 'Women']

    count_men = frame_men['Athlete'].value_counts().nlargest(1).to_dict()
    count_women = frame_women['Athlete'].value_counts().nlargest(1).to_dict()

    return {**count_men, **count_women}


# def main():
#     print('I''m grateful for everything ...')

#     ret = athletes_most_medals()
#     assert len(ret) == 2
#     assert ret["LATYNINA, Larisa"] == 18
#     assert ret["PHELPS, Michael"] == 22


# if __name__ == '__main__':
#     main()
