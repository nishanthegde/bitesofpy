from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class CrontabScheduler:
    """A scheduler based on cron expressions.

    The scheduler can be used to get the next scheduled datetime based on a reference datetime now.

    Attributes:
        expr (str): A valid cron expression (with four parts only, we dont use the fifth part in this bite).
        now (datetime): The reference datetime for which the next datetime should be determined.
        ... hopefully more attributes added by you!

    Raises:
        ValueError: Whenever a value for a cron expression part is not valid.
    """

    expr: str
    now: datetime

    def __iter__(self):
        return self

    def __next__(self) -> datetime:
        # Right now this returns the input datetime now, so you can run all tests and see how it works.
        # However, you are supposed to implement your own logic here to return the next
        # datetime according to the bite description.
        parts = self.expr.split()
        every_min_flag = 0
        every_hour_flag = 0
        every_day_flag = 0

        if parts[0] == '*':
            every_min_flag = 1
            next_at = self.now + timedelta(minutes=1)
        else:
            delta_minutes = 60 - self.now.minute + int(parts[0].strip())
            next_at = self.now + timedelta(minutes=delta_minutes)

        if parts[1] == '*':
            every_hour_flag = 1
            pass
        else:
            # check if hour of reference is the same as hour in cron expression
            if int(parts[1].strip()) == self.now.hour:
                # hour is the same as what is specified for min in cron expression
                if every_min_flag == 1:  # if every_min_flag is set then go to the next minute
                    delta_minutes = 1
                    next_at = self.now + timedelta(minutes=delta_minutes)
                else:  # otherwise check if current minute is less than minute specified in the first part
                    if self.now.minute < int(parts[0].strip()):
                        delta_minutes = int(parts[0].strip()) - self.now.minute
                        next_at = self.now + timedelta(minutes=delta_minutes)
                    else:  # otherwise go to next day to the minute specified in the first part
                        delta_minutes = ((23 - self.now.hour) * 60) + (60 - self.now.minute) + (
                                int(parts[1].strip()) * 60) + int(parts[0].strip())
                        next_at = self.now + timedelta(minutes=delta_minutes)
            else:
                # hour is the not the same go to hour in the cron expression
                if every_min_flag == 1:  # if every_min_flag is set then go to minute 0
                    delta_minutes = ((23 - self.now.hour) * 60) + (60 - self.now.minute) + (int(parts[1].strip()) * 60)
                    next_at = self.now + timedelta(minutes=delta_minutes)
                else:  # otherwise go to minute specified in the first part
                    delta_minutes = ((23 - self.now.hour) * 60) + (60 - self.now.minute) + (
                            int(parts[1].strip()) * 60) + int(parts[0].strip())
                    next_at = self.now + timedelta(minutes=delta_minutes)

        if parts[2] == '*':
            every_day_flag = 1
            pass
        else:
            # check if day of reference is the same as day in cron expression
            if int(parts[2].strip()) == self.now.day:
                # day is the same as what is specified for day in cron expression
                if every_hour_flag == 1:  # if every_hour_flag is set then go to the next minute
                    if every_min_flag == 1:  # if every_min_flag is set then go to the next minute
                        delta_minutes = 1
                        next_at = self.now + timedelta(minutes=delta_minutes)
                    else:  # otherwise check if current minute is less than minute specified in the first part
                        if self.now.minute < int(parts[0].strip()):
                            delta_minutes = int(parts[0].strip()) - self.now.minute
                            next_at = self.now + timedelta(minutes=delta_minutes)
                        else:  # otherwise go to next day to the minute specified in the first part
                            delta_minutes = ((23 - self.now.hour) * 60) + (60 - self.now.minute) + (
                                    int(parts[1].strip()) * 60) + int(parts[0].strip())
                            next_at = self.now + timedelta(minutes=delta_minutes)
                else:  # otherwise check if current hour is less than hour specified in the second part
                    pass
            else:
                # day is not the same as what is specified for day in cron expression
                # if every_hour_flag == 1:  # if every_hour_flag is set then go to hour 0
                #     if every_min_flag == 1:  # if every_min_flag is set then go to minute 0 of specified day
                #         delta_minutes = ((23 - self.now.hour) * 60) + (60 - self.now.minute) + (int(parts[1].strip()) * 60)
                #         next_at = self.now + timedelta(minutes=delta_minutes)
                #     else:  # otherwise ...
                #         pass
                # else:  # otherwise check if current hour is less than hour specified in the second part
                #     pass
                pass

        return next_at


def main():
    print("thank you for everything!")

    # cron_expr = "* * * *"
    # ref_date = datetime(2022, 6, 1, 12, 12)
    # it = CrontabScheduler(cron_expr, ref_date)
    # print(next(it))
    #
    # cron_expr = "10 * * *"
    # ref_date = datetime(2022, 6, 1, 12, 12)
    # it = CrontabScheduler(cron_expr, ref_date)
    # print(next(it))

    # cron_expr = "* 5 * *"
    # ref_date = datetime(2022, 6, 1, 12, 12)
    # it = CrontabScheduler(cron_expr, ref_date)
    # print(next(it))
    #
    # cron_expr = "9 5 * *"
    # ref_date = datetime(2022, 6, 1, 12, 12)
    # it = CrontabScheduler(cron_expr, ref_date)
    # print(next(it))
    #
    # cron_expr = "* 12 * *"
    # ref_date = datetime(2022, 6, 1, 12, 12)
    # it = CrontabScheduler(cron_expr, ref_date)
    # print(next(it))
    #
    # cron_expr = "14 12 * *"
    # ref_date = datetime(2022, 6, 1, 12, 12)
    # it = CrontabScheduler(cron_expr, ref_date)
    # print(next(it))

    cron_expr = "* * 21 *"
    ref_date = datetime(2022, 6, 1, 12, 12)
    it = CrontabScheduler(cron_expr, ref_date)
    print(next(it))


if __name__ == '__main__':
    main()
