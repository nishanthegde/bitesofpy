from event import get_attendees


def test_get_attendees(capfd):
    get_attendees()
    output = capfd.readouterr()[0].strip().split("\n")

    assert len(output) == 8
    assert "('Kim', '-', '-')" in output
    assert "('Andre', '-', '-')" in output


def main():
    print('thank you for everything ... ')


if __name__ == '__main__':
    main()
