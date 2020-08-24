def calculate_score(frames: str) -> int:
    """Calculates a total 10-pin bowling score from a string of frame data."""
    score = {}  # dict to store all scores key=frame, value=[roll 1 score, roll 2 score, frame_score, bonus]
    frame = 1  # counter for frame number
    roll = 1  # counter for roll number

    # initialize frame score to 0, roll score to 0
    frame_score = 0
    roll_score = 0

    # flag to indicate whether strike or spare
    # bonus =  1 spare 2 strike
    bonus = 0
    for i, s in enumerate(frames):
        # print(i, frame, roll)

        if s != ' ':
            if s == '-':
                roll_score = 0
            elif s == 'X':
                roll_score = 10
                bonus = 2
            elif s == '/':
                roll_score = 10 - frame_score
                bonus = 1
            else:
                roll_score = int(s)

        frame_score += roll_score

        if frame == 11:
            roll1_score = roll_score
            roll2_score = 0
            score[frame] = list((roll1_score, roll2_score, frame_score, bonus))

        # insert frame score if 2ndd roll
        if roll == 2:
            roll2_score = roll_score
            score[frame] = list((roll1_score, roll2_score, frame_score, bonus))
        else:
            roll1_score = roll_score

        # print('frame:{} score:{} bonus:{}'.format(frame, frame_score, bonus))

        if i % 2 != 0:
            # increment frame number set frame score to 0, roll number to first roll, set bonus to 0 for new frame
            frame += 1
            frame_score = 0
            roll = 1
            bonus = 0
        else:
            # increment roll number to second roll set roll score to 0
            roll += 1
            roll_score = 0

    # print(score)

    # update scores with bonus values
    for k, v in score.items():
        # if bonus is spare
        if v[3] == 1:
            # not last frame
            if k < 11:
                # update score with roll 1 score from next frame do this even for 10th frame
                v[2] += score[k + 1][0]
            else:
                # last frame
                v[2] = 10 - score[k - 1][1]

        # if bonus is strike
        if v[3] == 2 and k <= 9:
            # first update score with roll 1 score from next frame 10th frame does not get updated
            v[2] += score[k + 1][0]
            # if the next frame has a roll 2 score or the next frame is 10
            if score[k + 1][1] > 0 or k + 1 == 10:
                v[2] += score[k + 1][1]
            else:
                # next frame does not have a roll 2 score either because a miss or strike
                # if the next frame is a strike
                if score[k + 1][3] == 2:
                    # then update score with roll 1 score from next frame
                    v[2] += score[k + 2][0]
                # else:
                #     # if the next frame is also a strike then get roll 1 score from the frame after next
                #     v[2] += score[k + 2][0]

    final = sum(score[frame][2] for frame in score if frame <= 10)

    # add last frame if 10th frame has a strike
    if score[10][3] == 2:
        final += score[11][2]

    # print(score)
    return final
