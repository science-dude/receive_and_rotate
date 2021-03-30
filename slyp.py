# A script that holds the result for the receive and rotate challenge.
import time
import itertools
from typing import Dict
from typing import List
from typing import Optional
from typing import Set

word_rotation_map_type = Dict[str, Set[str]]
word_length_map_type = Dict[int, word_rotation_map_type]


class Slyp:
    """
    The class is capable of receiving and storying words in memory.
    It can also run rotation analysis printing a list of list of matching 
    rotations.
    """

    def __init__(self):
        super().__init__()
        # Help to categorise words based on length for faster computation
        self.word_length_map: word_length_map_type = {}
        self.list_of_unique_words: Set = set()

    def receive_word(self, word: str) -> None:
        """Evaluates a word and stores it in the instance if applicable"""
        word = word.lower().strip()
        if not self.is_word_valid(word):
            print(f"Such great program will not store invalid words like: `{word}`")
            return

        if self.check_if_was_evaluated_before(word):
            print(f"We have already investigated: {word}")
            return

        word_length = len(word)
        # Check if a word this long was evaluated before
        if not self.word_length_map.get(word_length):
            # Create a word rotation map with an initial value
            self.word_length_map[word_length] = {word: set([word])}
            return

        self.store_in_rotation_map(self.word_length_map[word_length], word)

    def store_in_rotation_map(
        self, specific_length_word_rotation_map: word_rotation_map_type, word: str
    ):
        """Stores a word in a rotation map for other funcions to retrieve"""
        if rotation := self.search_for_rotations(
            specific_length_word_rotation_map, word
        ):
            # If rotation exist add the word to the rotations
            rotation.add(word)
        else:
            # If rotation doesn't exist create a set of words
            specific_length_word_rotation_map[word] = set(
                [word]
            )

    def get_rotations(self) -> List[Set[str]]:
        """
        Returns all the words that happen to be rotations of
        other words in a desired format
        """
        all_rotations = []
        for rotation_map in self.word_length_map.values():
            all_rotations.append([list(value) for value in rotation_map.values()])
        return list(itertools.chain.from_iterable(all_rotations))

    def is_word_valid(self, word: str) -> bool:
        """Validates strings against the word criteria"""
        if any([len(word) < 1, not word.isalpha()]):
            return False
        return True

    def check_if_was_evaluated_before(self, word: str) -> bool:
        """Checks if a string was received by this instance of the class"""
        size_before = len(self.list_of_unique_words)
        self.list_of_unique_words.add(word)
        size_after = len(self.list_of_unique_words)
        return size_after == size_before

    def is_a_rotation(self, word: str, rotation_of: str) -> bool:
        return word in rotation_of * 2

    def search_for_rotations(self, word_rotation_map, word: str) -> Optional[Set[str]]:
        """
        Returns a set of words that fits a word in terms of rotations.
        Return None if a matching set does not exist.
        """
        for unique_word in word_rotation_map.keys():
            if self.is_a_rotation(word, unique_word):
                return word_rotation_map[unique_word]
        return None


if __name__ == "__main__":
    slyp = Slyp()
    print("To exit type `exit`. To display current rotations type `rotations`")
    while True:
        word = input("Ready to receive a word...   ")
        if word == "exit":
            break
        elif word == "rotations":
            print(slyp.get_rotations())
        else:
            slyp.receive_word(word)

        time.sleep(0.1)

