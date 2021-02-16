from typing import Union
import pathlib
from io import StringIO
import csv
import re

# Extracted from https://en.wikipedia.org/wiki/List_of_file_signatures
MAGIC_IMAGE_TABLE = """
"magic_bytes","text_representation","offset","extension","description"
"47 49 46 38 37 61
47 49 46 38 39 61","GIF87a
GIF89a",0,"gif","Image file encoded in the Graphics Interchange Format (GIF)"
"FF D8 FF DB
FF D8 FF E0 00 10 4A 46 49 46 00 01
FF D8 FF EE
FF D8 FF E1 ?? ?? 45 78 69 66 00 00","ÿØÿÛ
ÿØÿà..JFIF..
ÿØÿîÿØÿá..Exif..",0,"jpg
jpeg","JPEG raw or in the JFIF or Exif file format"
"89 50 4E 47 0D 0A 1A 0A",".PNG....",0,"png","Image encoded in the Portable Network Graphics format"
"49 49 2A 00 (little-endian format)
4D 4D 00 2A (big-endian format)","II*.MM.*",0,"tif
tiff","Tagged Image File Format (TIFF)"
"50 31 0A","P1.",0,"pbm","Portable bitmap"
"""  # noqa: E501

CUSTOM_MAGIC_TABLE2 = """
"magic_bytes","text_representation","offset","extension","description"
"01 70 79 62 69 74 65 73 00 01 22 ?? ?? ?? 66 6F 72 6D 61 74 (little endian)
01 70 79 62 69 74 65 73 01 00 22 ?? ?? ?? 66 6F 72 6D 61 74 (big endian)",".pybites..""...format
.pybites..""...format","1","pybites
pbf2","Fantasy pybites file format"
"""  # noqa: E501


class FileNotRecognizedException(Exception):
    """
    File cannot be identified using a magic table
    """
    pass


def determine_filetype_by_magic_bytes(
        file_name: Union[str, pathlib.Path],
        lookup_table_string: str = MAGIC_IMAGE_TABLE,
) -> str:
    """
    file_name: file name with path
    lookup_table_string: a comma separated text containing a magic table

    Returns: file format based on the magic bytes
    """

    no_matches = True

    bytes = open(file_name, "rb").read(32)
    hex_bytes = " ".join(['{:02X}'.format(byte) for byte in bytes])
    # print(hex_bytes)

    magic = StringIO(lookup_table_string)
    reader = csv.reader(magic, delimiter=',')

    next(reader, None)
    next(reader, None)

    for row in reader:
        parsed_row = [element.split('\n') for element in row]
        parsed_row.insert(0, [re.sub(r"\s*[\(].*?[\)\]]", "", byte_seq) for byte_seq in parsed_row[0]])
        parsed_row.pop(1)
        # print(parsed_row)
        for byte_seq in parsed_row[0]:
            regex = re.compile(byte_seq.replace('?', '.'))
            # if byte_seq in hex_bytes:
            if re.search(regex, hex_bytes):
                no_matches = False
                return parsed_row[4][0]

    if no_matches:
        raise FileNotRecognizedException('File format not recognized')


def main():
    print('thank you for looking after my mama :-)')


# Set up for your convenience when coding:
#  - creates a test_image.gif GIF file
#  - calls determine_filetype_by_magic_bytes
#  - prints out file type

if __name__ == "__main__":
    # test_filename = "test_image.gif"
    # print(f"Script invoked directly. Writing out test file {test_filename}")
    # with open(test_filename, "wb") as f:
    #     f.write(
    #         b"\x47\x49\x46\x38\x37\x61\x01\x00x01\x00\x80\x00\x00\xff\xff\xff"
    #         b"\xff\xff\xff\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02"
    #         b"\x44\x01\x00\x3b"
    #     )
    # print("Testing file format")
    # print(determine_filetype_by_magic_bytes(test_filename))

    # test_filename = "test_image.png"
    # print(f"Script invoked directly. Writing out test file {test_filename}")
    # with open(test_filename, "wb") as f:
    #     f.write(
    #             b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00"
    #             b"\x00\x01\x08\x04\x00\x00\x00\xb5\x1c\x0c\x02\x00\x00\x00"
    #             b"\x0bIDATx\xdac\xfc\xff\x1f\x00\x03\x03\x02\x00\xef\xa2\xa7["
    #             b"\x00\x00\x00\x00IEND\xaeB`\x82"
    #     )
    # print("Testing file format")
    # print(determine_filetype_by_magic_bytes(test_filename))

    test_filename = "test_image.pybites"
    print(f"Script invoked directly. Writing out test file {test_filename}")
    with open(test_filename, "wb") as f:
        f.write(
            b'\xee\x01pybites\x00\x01"\x00\xec\xedformat\x01\x00\x00\x00'
            b"\x00\x01"
        )
    print("Testing file format")
    print(determine_filetype_by_magic_bytes(test_filename, CUSTOM_MAGIC_TABLE2))

    main()
