import os
from pathlib import Path
from typing import List
import unicodedata
from urllib.request import urlretrieve


def _get_spanish_dictionary_words() -> List[str]:
    filename = "spanish.txt"
    # source of file
    # https://raw.githubusercontent.com/bitcoin/bips
    # /master/bip-0039/spanish.txt
    url = f"https://bites-data.s3.us-east-2.amazonaws.com/{filename}"
    tmp_folder = os.getenv("TMP", "/tmp")
    local_filepath = Path(tmp_folder) / filename
    if not Path(local_filepath).exists():
        urlretrieve(url, local_filepath)
    return local_filepath.read_text().splitlines()


SPANISH_WORDS = _get_spanish_dictionary_words()


def get_accentuated_sentence(
        text: str, words: List[str] = SPANISH_WORDS
) -> str:
    output_str = text

    # decode each spanish word
    spanish_words_decoded = []
    for sw in SPANISH_WORDS:
        nfkd_form = unicodedata.normalize('NFKD', sw)
        spanish_words_decoded.append(u"".join([c for c in nfkd_form if not unicodedata.combining(c)]))

    for word in text.split():
        trim_word = ''.join(c for c in word if c.isalnum())
        # print(trim_word)
        if trim_word in spanish_words_decoded:
            idx_trim_word = spanish_words_decoded.index(trim_word)
            output_str = output_str.replace(trim_word, SPANISH_WORDS[idx_trim_word])

    return output_str
