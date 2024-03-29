from dataclasses import dataclass
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


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
        every_month_flag = 0

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

        # check day(month) part of cron expression

        if parts[2] == '*':  # if star than set daily flag
            every_day_flag = 1
            pass
        else:  # a number is specified in day(month) part of cron
            # check if day in reference datetime is the same as day in day(month) part of expression

            if int(parts[2].strip()) == self.now.day:  # if day is the same
                # check what was specified in the hour and month parts of the expression

                if every_hour_flag == 1:  # if every_hour_flag is set then go to the next minute
                    if every_min_flag == 1:  # if every_min_flag is set then go to the next minute
                        delta_minutes = 1
                        next_at = self.now + timedelta(minutes=delta_minutes)
                    else:  # a number is specified in the minute part
                        # check if minute in reference datetime is less than minute in cron expression

                        if self.now.minute < int(parts[0].strip()):  # if ref min is less than cron min
                            delta_minutes = int(parts[0].strip()) - self.now.minute
                            next_at = self.now + timedelta(minutes=delta_minutes)
                        else:  # otherwise go to next day to the minute specified in the first part
                            pass
                            return None
                else:  # a number is specified in hour part of cron
                    pass
            else:
                # day is not the same

                # check what was specified in the hour and minute parts of the expression

                if every_hour_flag == 1:  # if every_hour_flag is set then go to hour 0
                    if every_min_flag == 1:  # if every_min_flag is set then go to minute 0
                        # check if day in reference datetime is less than day in cron expression

                        if self.now.day < int(parts[2].strip()):  # if ref day is less than cron day
                            delta_days = int(parts[2].strip()) - self.now.day
                            next_at = self.now + timedelta(days=delta_days)
                            next_at = datetime(next_at.year, next_at.month, next_at.day, 0, 0)
                        elif self.now.day == int(parts[2].strip()):  # if ref day is same as cron day
                            delta_minutes = 1
                            next_at = self.now + timedelta(minutes=1)
                        else:  # ref day is less than cron day
                            # go to cron day in next month
                            delta_months = 1
                            next_at = self.now + relativedelta(months=delta_months)
                            next_at = datetime(next_at.year, next_at.month, int(parts[2].strip()), 0, 0)
                    else:  # a number is specified in the minute part
                        # check if minute in reference datetime is less than minute in cron expression
                        pass
                        return None
                else:  # a number is specified in hour part of cron
                    pass

        # check month part of cron expression

        if parts[3] == '*':  # if star than set monthly flag
            every_month_flag_flag = 1

            if every_day_flag == 1:
                if every_hour_flag == 1:  # if every_hour_flag is set then go to the next minute
                    if every_min_flag == 1:  # if every_min_flag is set then go to the next minute
                        pass
                    else:
                        # a number is specified in the minute part
                        pass
                else:
                    # a number is specified in hour part of cron
                    pass
            else:
                # a number is specified in day part of cron
                if self.now.day < int(parts[2].strip()):  # if ref day is less than cron day
                    delta_months = 0
                else:
                    delta_months = 1
                next_day = int(parts[2].strip())

                if every_hour_flag == 1:  # if every_hour_flag is set
                    pass
                else:
                    # a number is specified in hour part of cron
                    next_hr = int(parts[1].strip())

                if every_min_flag == 1:  # if every_min_flag is set then go to the next minute
                    pass
                else:
                    # a number is specified in the minute part
                    next_min = int(parts[0].strip())

            next_at = self.now + relativedelta(months=delta_months)
            next_at = datetime(next_at.year, next_at.month, next_day, next_hr, next_min)

        else:
            # a number is specified in month part of cron
            # check if month in reference datetime is the same as month in mont part of expression

            if int(parts[3].strip()) == self.now.month:

                # if month is the same
                # check what was specified in the day, hour and min parts of the expression

                if every_day_flag == 1:
                    if every_hour_flag == 1:  # if every_hour_flag is set then go to the next minute
                        if every_min_flag == 1:  # if every_min_flag is set then go to the next minute
                            delta_minutes = 1
                            next_at = self.now + timedelta(minutes=delta_minutes)
                        else:  # a number is specified in the minute part
                            # check if minute in reference datetime is less than minute in cron expression

                            if self.now.minute < int(parts[0].strip()):  # if ref min is less than cron min
                                delta_minutes = int(parts[0].strip()) - self.now.minute
                                next_at = self.now + timedelta(minutes=delta_minutes)
                            else:  # otherwise go to next day to the minute specified in the first part
                                pass
                                return None
                    else:  # a number is specified in hour part of cron
                        pass
                else:  # a number is specified in day part of cron
                    pass
            else:
                # month is not the same

                # check what was specified in the day, hour and min parts of the expression
                if every_day_flag == 1:
                    if every_hour_flag == 1:  # if every_hour_flag is set then go to hour 0
                        if every_min_flag == 1:  # if every_min_flag is set then go to minute 0

                            # check if month in reference datetime is less than month in cron expression

                            if self.now.month < int(parts[3].strip()):  # if ref month is less than cron month
                                delta_months = int(parts[3].strip()) - self.now.month
                                next_at = self.now + relativedelta(months=delta_months)
                                next_at = datetime(next_at.year, next_at.month, 1, 0, 0)
                            elif self.now.month == int(parts[3].strip()):  # if ref month is same as month
                                delta_minutes = 1
                                next_at = self.now + timedelta(minutes=1)
                            else:  # ref month is more than cron month
                                # go to cron month in next year
                                delta_years = 1
                                next_at = self.now + relativedelta(years=delta_years)
                                next_at = datetime(next_at.year, int(parts[3].strip()), 1, 0, 0)
                        else:

                            # a number is specified in the minute part

                            if self.now.month < int(parts[3].strip()):  # if ref month is less than cron month
                                delta_months = int(parts[3].strip()) - self.now.month
                                next_at = self.now + relativedelta(months=delta_months)
                                next_at = datetime(next_at.year, next_at.month, 1, 0, int(parts[0].strip()))
                            elif self.now.month == int(parts[3].strip()):  # if ref month is same as month
                                delta_minutes = 1
                                next_at = self.now + timedelta(minutes=1)
                            else:  # ref month is more than cron month
                                # go to cron month in next year
                                delta_years = 1
                                next_at = self.now + relativedelta(years=delta_years)
                                next_at = datetime(next_at.year, int(parts[3].strip()), 1, 0, int(parts[0].strip()))
                    else:  # a number is specified in hour part of cron
                        pass
                else:  # a number is specified in day part of cron
                    pass

        return next_at


def main():
    print("thank you for everything!")

    cron_expr = "15 14 30 *"
    ref_date = datetime(2022, 6, 28, 19, 49)
    it = CrontabScheduler(cron_expr, ref_date)
    print(next(it))


if __name__ == '__main__':
    main()
