def calculate_score(frames: str) -> int:
    """Calculates a total 10-pin bowling score from a string of frame data."""
    score = {}  # dict to store all scores key=frame, value=frame_score
    frame = 1  # counter for frame number
    roll = 1  # counter  for roll number

    # initialize frame score to 0, roll score to 0
    frame_score = 0
    roll_score = 0

    for i, s in enumerate(frames):
        print(i, frame, roll)
        if s != ' ':
            if s == '-':
                roll_score = 0
            elif s == 'X':
                roll_score = 10
            elif s == '/':
                roll_score = 10 - frame_score
            else:
                roll_score = int(s)

        frame_score += roll_score

        print('frame:{} score:{}'.format(frame, frame_score))

        if i % 2 != 0:
            # increment frame number set frame score to 0, roll number to first roll
            frame += 1
            print('\n')
            frame_score = 0
            roll = 1
        else:
            # increment roll number to second roll set roll score to 0
            roll += 1
            roll_score = 0

    return score


def main():
    print('thank you for the waves this morning and thank you for looking after my mama...')
    # print(calculate_score('--------------------'))
    print(calculate_score('8/9-X X 6/4/X 8-X XXX'))


if __name__ == "__main__":
    main()
