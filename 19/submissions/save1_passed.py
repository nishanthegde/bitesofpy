import inspect
from datetime import datetime, timedelta

NOW = datetime.now()


class Promo:

    def __init__(self, name: str, expires: datetime):
        self.name = name
        self.expires = expires

    @property
    def expired(self):
        """Get the current voltage."""
        return self.expires < NOW


# def main():
#     print('thank you for everything ...')
#     past_time = NOW - timedelta(seconds=3)
#     # print(past_time)
#     # print(type(past_time))

#     twitter_promo = Promo('twitter', past_time)
#     assert twitter_promo.expired

#     future_date = NOW + timedelta(days=1)
#     newsletter_promo = Promo('newsletter', future_date)
#     assert not newsletter_promo.expired

#     assert 'property' in inspect.getsource(Promo)


# if __name__ == '__main__':
#     main()
