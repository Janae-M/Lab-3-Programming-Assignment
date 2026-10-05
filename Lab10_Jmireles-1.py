"""
Word Count Program
Janae Mireles
OOP-based program that displays a menu of 4 predefined text files, lets the user choose one, then reads and analyzes that file. 
October 4th, 2026
"""
from pathlib import Path
import string

class WordAnalyzer:
    def __init__(self, filepath, stop_words=None):
        self.__filepath = Path(filepath)
        self.__frequencies = {}
        self.__stop_words = set(stop_words) if stop_words else set()

    def process_file(self):
        try:
            if not self.__filepath.exists():
                raise FileNotFoundError

            translation_table = str.maketrans('', '', string.punctuation)

            with self.__filepath.open('r', encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    line = line.translate(translation_table)
                    words = line.split()

                    for word in words:
                        if word not in self.__stop_words:
                            if word in self.__frequencies:
                                self.__frequencies[word] += 1
                            else:
                                self.__frequencies[word] = 1

            return True

        except FileNotFoundError:
            print(f"File not found: {self.__filepath}")
            return False

    def print_report(self):
        words = sorted(self.__frequencies.keys())

        for word in words:
            print(f"{word:<10} :: {self.__frequencies[word]}")

    