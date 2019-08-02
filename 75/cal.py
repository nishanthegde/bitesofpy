def get_weekdays(calendar_output):
    """Receives a multiline Unix cal output and returns a mapping (dict) where
       keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)"""

    weekdays = {}

    # list of cal lines in multi line input
    cal_lines = calendar_output.split('\n')
    # print(cal_lines)
    cal_keys =  [(l[0:2], l[3:5], l[6:8], l[9:11], l[12:14], l[15:17], l[18:20]) for l in cal_lines[2:-1]]
    # print(cal_keys)
    cal_days = cal_lines[1].split()
    # print(cal_days)

    return {int(k[i].strip()):cal_days[i] for k in cal_keys for i in range(7) if k[i].strip() != ''}

# def main():

#     weekdays = get_weekdays(april_1981)
#     assert len(weekdays) == 30
#     assert weekdays[25] == 'Sa'
#     assert weekdays[22] == 'We'

#     weekdays = get_weekdays(jan_1986)
#     assert len(weekdays) == 31
#     assert weekdays[20] == 'Mo'
#     assert weekdays[16] == 'Th'

#     weekdays = get_weekdays(jan_1956)
#     assert len(weekdays) == 31
#     assert weekdays[13] == 'Fr'
#     assert weekdays[31] == 'Tu'

# if __name__ == "__main__":
#     main()

