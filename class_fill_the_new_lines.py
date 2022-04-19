"""
This script solves the problem that when copy-pasting from pdf files, texts come in
line by line as new lines. Makes text copied from pdf to be on a single line.
Created by AKE - 19.04.22
"""


class FillTheNewLines:
    """
    This class solves the problem that when copy-pasting from pdf files, texts come in
    line by line as new lines. Makes text copied from pdf to be on a single line.
    """

    def __init__(self, file_name):
        self.file_name = file_name

    def main(self):
        """
        Reads the file of raw text and returns the text.
        """
        with open(self.file_name, "r", encoding="UTF-8") as file:
            text = file.read()
        return self.delete_new_lines(text)

    def delete_new_lines(self, text):
        """
        Deletes all new lines from the raw text.
        """
        text = text.replace("\n", " ")
        return self.write_to_file(text, "output.txt")

    @classmethod
    def write_to_file(cls, text, output_file_name):
        """
        Writes the revised text to the output file.
        """
        with open(output_file_name, "w", encoding="UTF-8") as file:
            file.write(text)
        return text


# FillTheNewLines("text.txt").main()
