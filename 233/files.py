from datetime import datetime
from pathlib import Path, PosixPath
from zipfile import ZipFile
import os
from time import sleep
import shutil
import glob
import re
local = '/tmp'
# local = os.getcwd()
TMP = Path('/tmp')
# TMP = Path(local)
LOG_DIR = TMP / 'logs'
ZIP_FILE = 'logs.zip'


def zip_last_n_files(directory: PosixPath = LOG_DIR,
                     zip_file: str = ZIP_FILE, n: int = 3):

    latest = sorted(list(filter(os.path.isfile, glob.glob(str(directory) + '/*'))), key=lambda x: os.path.getmtime(x), reverse=True)[:n]

    # for f in latest:
    #     d = datetime.fromtimestamp(os.path.getmtime(f))
    #     print(d.strftime('%Y-%m-%d'))

    with ZipFile(zip_file, 'w') as zp:
        for f in latest:
            d = datetime.fromtimestamp(os.path.getmtime(f))
            zp.write(f, '{}_{}.{}'.format(os.path.basename(f).split('.')[0], d.strftime('%Y-%m-%d'), os.path.basename(f).split('.')[1]))

    return latest


def main():
    print('thank you for everything ...')
    # print(LOG_DIR)

    log_dir = LOG_DIR

    if os.path.exists(log_dir):
        shutil.rmtree(log_dir)

    log_dir.mkdir()

    # for i in range(1, 10, 2):
    #     sleep(0.01)
    #     p = log_dir / f"{i}.log"
    #     p.write_text('log line')

    for i in range(20, 6, -3):
        sleep(0.01)
        p = log_dir / f"{i}.log"
        p.write_text('log line')

    zip_file = log_dir / ZIP_FILE
    zip_last_n_files(directory=log_dir, zip_file=zip_file, n=2)
    # print(ZipFile(zip_file).namelist())

    zip_ = ZipFile(zip_file)
    files = sorted(zip_.namelist())
    print(files)
    # assert len(files) == 3
    # f1, f2, f3 = files
    # assert re.match(r'^5_\d{4}-\d{2}-\d{2}.log$', f1)
    # assert re.match(r'^7_\d{4}-\d{2}-\d{2}.log$', f2)
    # assert re.match(r'^9_\d{4}-\d{2}-\d{2}.log$', f3)

    assert len(files) == 2
    f1, f2 = files
    assert re.match(r'^11_\d{4}-\d{2}-\d{2}.log$', f1)
    assert re.match(r'^8_\d{4}-\d{2}-\d{2}.log$', f2)


if __name__ == '__main__':
    main()
