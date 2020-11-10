"""Layne Keegan; CS 118; Project 1; This program searches for large duplicate files in a directory. These duplicate
files, if deleted, could recover wasted disk space."""
# noinspection PyUnresolvedReferences
from os.path import getsize, join
from time import time
# noinspection PyUnresolvedReferences
from p1utils import all_files, compare

pathname = "C:/Users/Layne/Downloads/"
biglist = all_files(pathname)


def search(file_list):
    """ Search command looks for duplicates within the file_list that was created by the all_files command from
    p1utils.py."""
    lol = []
    while 0 < len(file_list):
        dups = [x for x in file_list if compare(file_list[0], x)]
        file_list = [x for x in file_list if not compare(file_list[0], x)]
        if 1 < len(dups):
            lol.append(dups)
    return lol


def faster_search(file_list):
    """Faster_search builds off of the search command. The idea is to do the same thing in a more efficient and timely
    manner. The outcome is still a list of large duplicate files."""
    file_sizes = list(map(getsize, file_list))
    file_list = list(filter(lambda x: 1 < file_sizes.count(getsize(x)), file_list))
    return search(file_list)


def report(lol):
    """ The report command gives a report on the duplicate files found from search/ faster_search. This will tell you
    all you need to know about the duplicate files found and their sizes."""
    if 0 < len(lol):
        print("---DUPLICATE FILE FINDER REPORT---")
        print("\n")
        big = max(lol, key=len)
        big.sort()
        print(f"The file with the most duplicates is: {big[0]}")
        print(f"There are {len(big) - 1} copies of this file")
        for i in range(1, len(big)):
            print(big[i])

        big = max(lol, key=lambda x: len(x) * getsize(x[0]))
        print("\n")
        print(
            f"The most disk space ({getsize(big[0]) * (len(big) - 1)}) could be recovered by deleting the copies of "
            f"this file: {big[0]}.")
        print(f"Here are its {len(big) - 1} copies:")
        for i in range(1, len(big)):
            print(big[i])
    else:
        print("No duplicates found.")
    print("\n")


if __name__ == '__main__':
    path = join(".", "images")

    t0 = time()
    report(search(biglist))
    print(f"Runtime: {time() - t0:.2f} seconds")

    print("\n\n .. and now w/ a faster search implementation:")

    t0 = time()
    report(faster_search(biglist))
    print(f"Runtime: {time() - t0:.2f} seconds")
