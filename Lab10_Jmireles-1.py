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

    def proce