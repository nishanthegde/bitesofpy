import os
import sys
from pathlib import Path
from urllib.request import urlretrieve
from zipfile import ZipFile

import typer

current_directory = os.getcwd()
final_directory = os.path.join(current_directory, r"tmp")

if not os.path.exists(final_directory):
    os.makedirs(final_directory)

TMP = Path(final_directory)
S3 = "https://bites-data.s3.us-east-2.amazonaws.com"


def _setup():
    data_zipfile = "357-data.zip"
    urlretrieve(f"{S3}/{data_zipfile}", TMP / data_zipfile)
    ZipFile(TMP / data_zipfile).extractall(TMP)
    sys.path.append(TMP)


_setup()

from tmp.algorithms import app as algo_app  # noqa E402
from tmp.comparisons import app as compare_app  # noqa E402

app = typer.Typer()
app.add_typer(algo_app, name="algorithms")
app.add_typer(compare_app, name="comparisons")

if __name__ == "__main__":
    app()
