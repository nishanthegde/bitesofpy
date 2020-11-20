from __future__ import annotations

import string
import re

EOL_PUNCTUATION = ".!?"

class Document:
    def __init__(self, lines=[]) -> None:
        # it is up to you how to implement this method
        # feel free to alter this method and its parameters to your liking
        self.lines = lines

    def add_line(self, line: str, index: int = None) -> Document:
        """Add a new line to the document.

        Args:
            line (str): The line,
                expected to end with some kind of punctuation.
            index (int, optional): The place where to add the line into the document.
                If None, the line is added at the end. Defaults to None.

        Returns:
            Document: The changed document with the new line.
        """
        if index is not None:
            self.lines.insert(index, line)
        else:
            self.lines.append(line)

        return self

    def swap_lines(self, index_one: int, index_two: int) -> Document:
        """Swap two lines.

        Args:
            index_one (int): The first line.
            index_two (int): The second line.

        Returns:
            Document: The changed document with the swapped lines.
        """
        swap_out = self.lines[index_one]
        self.lines[index_one] = self.lines[index_two]
        self.lines[index_two] = swap_out

        return self

    def merge_lines(self, indices: list) -> Document:
        """Merge several lines into a single line.

        If indices are not in a row, the merged line is added at the first index.

        Args:
            indices (list): The lines to be merged.

        Returns:
            Document: The changed document with the merged lines.
        """
        to_merge = ""

        for i in sorted(indices):
            to_merge += self.lines[i] + " "

        # print(to_merge)
        # Pop lines that need to be merged
        for i in sorted(indices, reverse=True):
            del self.lines[i]

        # Insert merged element at first index position
        self.lines.insert(indices[0], to_merge.strip())

        return self

    def add_punctuation(self, punctuation: str, index: int) -> Document:
        """Add punctuation to the end of a sentence.

        Overwrites existing punctuation.

        Args:
            punctuation (str): The punctuation. One of EOL_PUNCTUATION.
            index (int): The line to change.

        Returns:
            Document: The document with the changed line.
        """

        if len(self.lines[index]) > 0 and self.lines[index][-1] in EOL_PUNCTUATION:
            self.lines[index] = self.lines[index][:-1] + punctuation
        else:
            self.lines[index] = self.lines[index] + punctuation

        return self

    def word_count(self) -> int:
        """Return the total number of words in the document."""
        word_count = 0

        for l in self.lines:
            print(re.findall(r'\w+', l))
            word_count += len(re.findall(r'\w+', l))

        return word_count

    @property
    def words(self) -> list:
        """Return a list of unique words, sorted and case insensitive."""

        words = []

        for l in self.lines:
            words += re.findall(r'\w+', l)

        return sorted(list(set([w.lower() for w in words])))

    def _remove_puctuation(line: str) -> str:
        """Remove punctuation from a line."""
        # you can use this function as helper method for
        # Document.word_count() and Document.words
        # or you can totally ignore it
        pass

    def __len__(self):
        """Return the length of the document (i.e. line count)."""
        return len(self.lines)

    def __str__(self):
        """Return the content of the document as string."""
        ret = ''
        for l in self.lines:
            ret += l + '\n'

        return ret.strip()


if __name__ == "__main__":
    print('thank you for looking after my mama!')

    # this part is only execute when you run the file and is ignored by the tests
    # you can use this section for debugging and testing
    #
    # d = (
    #     Document()
    #         .add_line("My second sentence.")
    #         .add_line("My first sentence.")
    #         .swap_lines(0, 1)
    #         .add_line("Introduction", 0)
    #         .add_punctuation("!", 0)
    #         .add_line("")
    #         .add_line("My second paragraph.")
    #         .merge_lines([1, 2])
    # )

    # d = (
    #     Document()
    #         .add_line("1")  # 1
    #         .add_line("2", 0)  # 2\n1
    #         .add_line("3", 1)  # 2\n3\n1
    #         .swap_lines(0, 1)  # 3\n2\n1
    #         .swap_lines(1, 2)  # 3\n1\n2
    #         .swap_lines(2, 1)  # 3\n2\n1
    #         .merge_lines([0, 2])  # 3 1\n2
    #         .merge_lines([0, 1])  # 3 1 2
    # )

    # d = (
    #     Document()
    #         .add_line("")
    #         .add_punctuation(".", 0)
    #     .add_punctuation("!", 0)
    #     .add_punctuation("?", 0)
    #     .add_line(".")
    #     .add_punctuation("?", 1)  # ?\n?
    # )

    # d = (
    #     Document().add_line("").swap_lines(0, 0).merge_lines([0]).add_punctuation(".", 0)
    #     )

    # d = (
    #     Document()
    #         .add_line("This is the tale of a dwarf.")
    #         .add_line("")
    #         .add_line("A dwarf you ask?")
    #         .add_line("Yes, a dwarf and not any dwarf, so you know!")
    # )

    # d = (
    #     Document()
    #         .add_line("first")
    #         .add_line("fourth")
    #         .add_line("third", 1)
    #         .add_line("second", 1)
    #
    # )
    #
    # print(d)
    # print(len(d))
    # print(d.word_count())
    # print(d.words)
