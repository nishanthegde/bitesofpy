import json
from contextlib import suppress
from dataclasses import dataclass
from ipaddress import AddressValueError, IPv4Address, IPv4Network
from pathlib import Path
from typing import List


@dataclass(frozen=True)
class ServiceIPRange:
    """
    Represents an IPv4 public network range, allocated by AWS for use with
    a specific service and region.
    """

    service: str
    region: str
    cidr: IPv4Network

    def __str__(self):
        return (f"{self.cidr} is allocated to the {self.service} "
                f"service in the {self.region} region")


def parse_ipv4_service_ranges(source: Path) -> List[ServiceIPRange]:
    """
    Given a JSON file containing AWS public IP addresses, return a list of
    ServiceIPRange objects representing all IPv4 network ranges. See also:

    https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html
    """
    data = json.loads(source.read_text())
    with suppress(AddressValueError):
        prefixes = data["prefixes"]
        ipv4_service_ranges = [
            ServiceIPRange(
                service=prefix["service"],
                region=prefix["region"],
                cidr=IPv4Network(prefix["ip_prefix"]),
            )
            for prefix in prefixes
        ]
    return ipv4_service_ranges


def get_aws_service_range(address: str,
                          service_ranges: list) -> List[ServiceIPRange]:
    """
    Return a list of ServiceIPRange objects representing all AWS public
    IP ranges that contain `address`. Raise a ValueError if `address`
    is not a valid IPv4 address.
    """
    try:
        ipv4_address = IPv4Address(address)
    except AddressValueError:
        raise ValueError("Address must be a valid IPv4 address")

    return [range_ for range_ in service_ranges
            if ipv4_address in range_.cidr]


def main():
    print('thank you for everything you have given me...')
    path = Path('/Users/nhegde/Google Drive/learning/self/bitesofpy/243/ip-ranges.json')
    # print(type(parse_ipv4_service_ranges(path)))
    # print(len(parse_ipv4_service_ranges(path)))
    # print(parse_ipv4_service_ranges(path)[0])
    # print(type(parse_ipv4_service_ranges(path)[0]))
    # print(type(IPv4Network('192.0.2.8/29')))
    # print(IPv4Network('192.0.2.8/29'))

    service_ranges = parse_ipv4_service_ranges(path)
    # print(service_ranges)
    address = 90.0
    # address = -100
    aws_service_ranges = get_aws_service_range(address, service_ranges)
    print(aws_service_ranges)
    # print(len(aws_service_ranges))
    # c = [r.cidr for r in aws_service_ranges]
    # print(IPv4Network('54.244.0.0/16') in c)

    # for r in aws_service_ranges:
    # assert
    # print(r)

    # print(aws_service_ranges[0])


if __name__ == "__main__":
    main()
