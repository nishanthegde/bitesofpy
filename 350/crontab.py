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

        if parts[0] == '*':
            every_min_flag = 1
            next_at = self.now + timedelta(minutes=1)
        else:
            delta_minutes = 60 - self.now.minute + int(parts[0].strip())
            next_at = self.now + timedelta(minutes=delta_minutes)

        if parts[1] == '*':
            pass
        else:
            # check if hour of reference is the same as hour in cron expression
            if int(parts[1].strip()) == self.now.hour:
                # hour is the same increment to what is specified for min in cron expression
                pass
            else:
                # hour is the not the same go to hour in the cron expression
                # delta_hours = 24 - self.now.hour + int(parts[1].strip())
                delta_minutes = ((23 - self.now.hour) * 60) + (60 - self.now.minute) + (int(parts[1].strip()) * 60)
                print(delta_minutes)
                next_at = self.now + timedelta(minutes=delta_minutes)

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

    cron_expr = "* 5 * *"
    ref_date = datetime(2022, 6, 1, 12, 12)
    it = CrontabScheduler(cron_expr, ref_date)
    print(next(it))


if __name__ == '__main__':
    main()
