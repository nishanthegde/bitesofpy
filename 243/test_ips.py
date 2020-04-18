import os
from pathlib import Path
from ipaddress import IPv4Network
from urllib.request import urlretrieve

import pytest
import sys

from ips import (ServiceIPRange, parse_ipv4_service_ranges,
                 get_aws_service_range)

URL = "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"

# local = os.getcwd()
local = '/tmp'
# TMP = os.getenv("TMP", "/tmp")

TMP = os.getenv("TMP", local)
PATH = Path(TMP, "ip-ranges.json")
IP = IPv4Network('192.0.2.8/29')

# print(PATH)
# print(IP)


@pytest.fixture(scope='module')
def json_file():
    """Import data into tmp folder"""
    urlretrieve(URL, PATH)
    return PATH


def test_json(json_file):
    assert str(json_file) != ''


def test_service_ips(json_file):
    ranges = parse_ipv4_service_ranges(json_file)
    assert len(ranges) == 1886
    assert type(ranges) == list
    assert all(isinstance(x, ServiceIPRange) for x in ranges)


def test_aws_service_range_with_valid_ip(json_file):
    ranges = parse_ipv4_service_ranges(json_file)
    address = '54.244.46.0'
    aws_service_ranges = get_aws_service_range(address, ranges)
    assert len(aws_service_ranges) == 3


def test_aws_service_range_with_invalid_ip(json_file):
    with pytest.raises(ValueError):
        ranges = parse_ipv4_service_ranges(json_file)
        address = '366.1.2.2'
        assert get_aws_service_range(address, ranges)


def test_aws_service_range_with_unable_to_find_address(json_file):
    ranges = parse_ipv4_service_ranges(json_file)
    address = '192.0.2.8'
    aws_service_ranges = get_aws_service_range(address, ranges)
    assert not aws_service_ranges


def test_out(json_file, capsys):
    ranges = parse_ipv4_service_ranges(json_file)
    address = '54.244.46.0'
    aws_service_ranges = get_aws_service_range(address, ranges)

    assert aws_service_ranges[0]

    print(aws_service_ranges[0])
    captured = capsys.readouterr()
    assert captured.out == '54.244.0.0/16 is allocated to the AMAZON service in the us-west-2 region\n'

# def test_aws_service_range_with_invalid_no_ip(json_file):
#     ranges = parse_ipv4_service_ranges(json_file)
#     with pytest.raises(ValueError) as exc:
#         address = ''
#         get_aws_service_range(address, ranges)
#         assert 'Address must be a valid IPv4 address' in str(exc)

# def test_aws_service_range_with_invalid_ip_message(json_file):
#     ranges = parse_ipv4_service_ranges(json_file)
#     with pytest.raises(ValueError) as exc:
#         address = '54.244.46.0'
#         assert get_aws_service_range(address, ranges)
#         # assert excinfo.value.message == 'oh no!'
#         # assert 'Address must be a valid IPv4 address' in str(exc)


# def test_aws_service_range_with_invalid_ip_message1(json_file):
#     ranges = parse_ipv4_service_ranges(json_file)
#     with pytest.raises(ValueError) as exc:
#         address = ''
#         get_aws_service_range(address, ranges)
#         assert exc.value.args[0] == 'oh no!'


# def test_aws_service_range_with_invalid_ip_message2(json_file):
#     ranges = parse_ipv4_service_ranges(json_file)
#     with pytest.raises(ValueError) as exc:
#         address = -10
#         assert get_aws_service_range(address, ranges)
