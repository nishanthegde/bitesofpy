import os

ONE_KB = 1024


def get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""
    f_list = []
    for path, dirs, files in os.walk(dirname):
        for f in files:
            size_bytes = os.path.getsize(os.path.join(path, f))
            print(size_bytes / ONE_KB)
            if size_bytes / ONE_KB >= size_in_kb:
                f_list.append(f)
            # print(path, f, )
    return f_list


def main():
    print('please look after everyone...')
    print([f for f in get_files('../115', .35)])


if __name__ == '__main__':
    main()
