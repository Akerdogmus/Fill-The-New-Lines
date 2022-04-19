"""
This code solves the problem that when copy-pasting from pdf files, texts come in
line by line as new lines. Makes text copied from pdf to be on a single line.
Created by AKE - 19.04.22
"""


def main(file_name):
    """
    Reads the file of raw text and returns the text.
    """
    with open(file_name, "r", encoding="UTF-8") as file:
        text = file.read()
        delete_new_lines(text)


def delete_new_lines(text):
    """
    Deletes all new lines from the raw text.
    """
    text = text.replace("\n", " ")
    write_to_file(text, "output.txt")


def write_to_file(text, file_name):
    """
    Writes the revised text to the output file.
    """
    with open(file_name, "w", encoding="UTF-8") as file:
        file.write(text)


main("text.txt")
