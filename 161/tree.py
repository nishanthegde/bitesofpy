import os
from tempfile import TemporaryDirectory

local = os.getcwd()
TMP = os.getenv("TMP", local)


def count_dirs_and_files(directory: str='.') -> tuple:
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    path, dirs, files = next(os.walk(directory))
    number_files = 0
    number_dir = 0
    for root, dirs, files in os.walk(directory):
        number_files += len(files)
        number_dir += len(dirs)

    return (number_dir, number_files)


# def main():
#     print('thank you for the waves...')
#     # print(local)
#     # print(type(local))
#     # print(TMP)
#     # print(type(TMP))

#     # for i in range(5):
#     #     filename = f'{i}.txt'
#     #     path = os.path.join(local, filename)
#     #     print(path)
#     #     with open(path, 'w') as f:
#     #         f.write('hello')
#     #         # print(filename)

#     # for i in range(5):
#     #     if not os.path.exists(os.path.join(local, str(i))):
#     #         os.makedirs(os.path.join(local, str(i)))

#     # path, dirs, files = next(os.walk(local))
#     # file_count = len(files)
#     # print(file_count)
#     # dir_count = len(dirs)
#     # print(dir_count)

#     with TemporaryDirectory(dir=TMP) as dirname:
#         for i in range(5):
#             filename = f'{i}.txt'
#             path = os.path.join(dirname, filename)
#             with open(path, 'w') as f:
#                 f.write('hello')
#         assert count_dirs_and_files(dirname) == (0, 5)
#         # print(count_dirs_and_files(dirname))

#     with TemporaryDirectory(dir=TMP) as dirname:
#         for i in range(5):
#             os.makedirs(os.path.join(dirname, str(i)))

#         assert count_dirs_and_files(dirname) == (5, 0)
#         # print(count_dirs_and_files(dirname))

#     with TemporaryDirectory(dir=TMP) as dirname:
#         for i in range(10):
#             if i % 2 == 0:
#                 target_dir = os.path.join(dirname, str(i))
#                 os.makedirs(target_dir)
#                 for j in range(5):
#                     filename = f'{j}.txt'
#                     path = os.path.join(target_dir, filename)
#                     with open(path, 'w') as f:
#                         f.write('hello')

#         assert count_dirs_and_files(dirname) == (5, 25)
#         # print(count_dirs_and_files(dirname))


# if __name__ == '__main__':
#     main()
