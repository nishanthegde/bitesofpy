import os
from pathlib import Path
from ipaddress import IPv4Network
from urllib.request import urlretrieve

import pytest

from ips import (ServiceIPRange, parse_ipv4_service_ranges,
                 get_aws_service_range)

URL = "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"
# local = os.getcwd()
local = '/tmp'
# TMP = os.getenv("TMP", "/tmp")
TMP = os.getenv("TMP", local)
PATH = Path(TMP, "ip-ranges.json")
IP = IPv4Network('192.0.2.8/29')

print(PATH)
print(IP)


@pytest.fixture(scope='module')
def json_file():
    """Import data into tmp folder"""
    urlretrieve(URL, PATH)
    return PATH


# write your pytest code ...
def test_service_ips(json_file):
    source_path = json_file
    ranges = parse_ipv4_service_ranges(source_path)
    assert len(ranges) == 1886
    assert type(ranges) == list
    assert all(isinstance(x, ServiceIPRange) for x in ranges)


def test_aws_service_range(json_file):
    source_path = json_file
    ranges = parse_ipv4_service_ranges(source_path)
    address = '54.244.46.0'
    aws_service_ranges = get_aws_service_range(address, ranges)
    assert len(aws_service_ranges) == 3
    c = [r.cidr for r in aws_service_ranges]
    assert IPv4Network('54.244.0.0/16') in c
