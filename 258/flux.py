import pandas as pd
XYZ = "https://bites-data.s3.us-east-2.amazonaws.com/xyz.csv"
THRESHOLDS = (5000, 0.05)


def calculate_flux(XYZ: str) -> list:
    """Read the data in from xyz.csv
    add two new columns, one to calculate dollar flux,
    and the other to calculate percentage flux
    return as a list of tuples
    """

    xyz_df = pd.read_csv(XYZ)

    xyz_df['dollar_flux'] = xyz_df['12/31/20'] - xyz_df['12/31/19']
    xyz_df['perc_flux'] = xyz_df['dollar_flux'] / xyz_df['12/31/19']

    return list(xyz_df.itertuples(index=False, name=None))


def identify_flux(xyz: list) -> list:
    """Load the list of tuples, iterate through
    each item and determine if it is above both
    thresholds. if so, add to the list
    """

    flagged_lines = []

    for t in xyz:
        # print(t)
        dollar_flux_crossed = 0
        perc_flux_crossed = 0
        if t[2] == 0:
            perc_flux_crossed = 1

        if abs(t[3]) > THRESHOLDS[0]:
            dollar_flux_crossed = 1

        if abs(t[4]) > THRESHOLDS[1]:
            perc_flux_crossed = 1

        if perc_flux_crossed == 1 and dollar_flux_crossed == 1:
            flagged_lines.append(t)

    return flagged_lines


def main():
    print('thank you for everything...')
    # calc = calculate_flux(XYZ)
    # print(calc)
    flux = identify_flux(calculate_flux(XYZ))
    print(flux)


if __name__ == '__main__':
    main()
