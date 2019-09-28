import re
import inspect

EMAIL_HEADER = """Return-Path: <bounces+5555-7602-redacted-info>
...
Received: by 10.8.49.86 with SMTP id mf9.22328.51C1E5CDF
    Wed, 19 Jun 2013 17:09:33 +0000 (UTC)
Received: from NzI3MDQ (174.37.77.208-static.reverse.softlayer.com [174.37.77.208])
by mi22.sendgrid.net (SG) with HTTP id 13f5d69ac61.41fe.2cc1d0b
for <redacted-info>; Wed, 19 Jun 2013 12:09:33 -0500 (CST)
Content-Type: multipart/alternative;
boundary="===============8730907547464832727=="
MIME-Version: 1.0
From: redacted-address
To: redacted-address
Subject: A Test From SendGrid
Message-ID: <1371661773.974270694268263@mf9.sendgrid.net>
Date: Wed, 19 Jun 2013 17:09:33 +0000 (UTC)
X-SG-EID: P3IPuU2e1Ijn5xEegYUQ...
X-SendGrid-Contentd-ID: {"test_id":"1371661776"}"""  # noqa E501

OTHER_HEADER = """
Return-Path: <info@pybit.es>
From: Bob & Julian from PyBites (info@pybit.es)
To: pybites@ninja.com
Subject: New regex learning path!
Date: Sun, 18 Aug 2019 17:16:10 -0700 (PDT)
Envelope-To: pybites@ninja.com
...
X-SendGrid-Contentd-ID: {"test_id":"1371661776"}
"""


def get_email_details(header: str) -> dict:
    """User re.search or re.match to capture the from, to, subject
       and date fields. Return the groupdict() of matching object, see:
       https://docs.python.org/3.7/library/re.html#re.Match.groupdict
       If not match, return None
    """

    match = re.search(r'^From:\s*(?P<from>.*)$[\s\S]*^To:\s*(?P<to>.*)$[\s\S]*^Subject:\s*(?P<subject>.*)$[\s\S]*^Date:\s*(?P<date>[^+-]+)\s', header, re.MULTILINE)

    if match:
        return match.groupdict()


# def main():

#     print('here ...')

#     src = inspect.getsource(get_email_details)
#     assert 're.match' in src or 're.search' in src
#     assert 'groupdict' in src

#     actual = get_email_details(EMAIL_HEADER)
#     expected = {'from': 'redacted-address',
#                 'to': 'redacted-address',
#                 'subject': 'A Test From SendGrid',
#                 'date': 'Wed, 19 Jun 2013 17:09:33'}
#     assert actual == expected

#     actual = get_email_details(OTHER_HEADER)
#     expected = {'from': 'Bob & Julian from PyBites (info@pybit.es)',
#                 'to': 'pybites@ninja.com',
#                 'subject': 'New regex learning path!',
#                 'date': 'Sun, 18 Aug 2019 17:16:10'}
#     assert actual == expected

#     assert get_email_details('bogus') is None


# if __name__ == '__main__':
#     main()
