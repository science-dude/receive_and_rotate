import unittest

from slyp import Slyp


class TestSlyp(unittest.TestCase):
    def setUp(self):
        self.slyp = Slyp()

    def test_initial_values(self):
        assert type(self.slyp.list_of_unique_words) == set
        assert len(self.slyp.list_of_unique_words) == 0
        assert self.slyp.word_length_map == {}

    def test_conditions_for_valid_word(self):
        assert self.slyp.is_word_valid("") is False
        assert self.slyp.is_word_valid("pap3r") is False
        assert self.slyp.is_word_valid("paper") is True
        assert self.slyp.is_word_valid("word_game") is False
        assert self.slyp.is_word_valid("word game") is False
        assert self.slyp.is_word_valid("wordgame") is True

    def test_if_a_word_was_evaluated_before(self):
        assert self.slyp.check_if_was_evaluated_before("paper") is False
        assert self.slyp.check_if_was_evaluated_before("paper") is True
        assert self.slyp.check_if_was_evaluated_before("Paper") is False

    def test_is_a_rotation(self):
        assert self.slyp.is_a_rotation("nab", "bna")
        assert self.slyp.is_a_rotation("", "")
        assert self.slyp.is_a_rotation("rotations", "srotation")
        assert self.slyp.is_a_rotation("rotations", "rsotation") is False
        assert self.slyp.is_a_rotation("exit", "texi")
        assert self.slyp.is_a_rotation("exit", "taxi") is False

    def test_searching_for_a_rotation_array(self):
        four_map = {
            "slyp": {"lyps", "psly", "slyp", "ypsl"},
            "lips": {"lips"},
            "cyan": {"cyan"},
        }  # example four letter map
        assert self.slyp.search_for_rotations(four_map, "saab") is None
        assert self.slyp.search_for_rotations(four_map, "saa") is None
        assert self.slyp.search_for_rotations(four_map, "saaby") is None
        self.assertSetEqual(
            self.slyp.search_for_rotations(four_map, "cyan"), set(["cyan"])
        )
        self.assertSetEqual(
            self.slyp.search_for_rotations(four_map, "lips"), set(["lips"])
        )
        self.assertSetEqual(
            self.slyp.search_for_rotations(four_map, "slyp"),
            set(["lyps", "psly", "slyp", "ypsl"]),
        )
        self.assertSetEqual(
            self.slyp.search_for_rotations(four_map, "lyps"),
            set(["lyps", "psly", "slyp", "ypsl"]),
        )

    def test_receive_word(self):
        # Test receive word stores information
        self.slyp.receive_word("dog")
        assert "dog" in self.slyp.list_of_unique_words
        self.slyp.list_of_unique_words.clear()

        # Stores upper case and lower vase as the same word
        assert len(self.slyp.list_of_unique_words) == 0
        self.slyp.receive_word("paper")  # stores only once per case
        self.slyp.receive_word("Paper")
        assert len(self.slyp.list_of_unique_words) == 1

        self.slyp.receive_word("Santa")  # stores in lower case
        assert len(self.slyp.list_of_unique_words) == 2
        assert "santa" in self.slyp.list_of_unique_words

        self.slyp.receive_word("wordgame ")  # strips whitelines
        assert len(self.slyp.list_of_unique_words) == 3
        assert "wordgame" in self.slyp.list_of_unique_words
        self.slyp.list_of_unique_words.clear()

    def test_word_length_map_storage(self):
        self.assertDictEqual(self.slyp.word_length_map, {})
        self.slyp.receive_word("wordgame")
        self.assertDictEqual(self.slyp.word_length_map, {8: {"wordgame": {"wordgame"}}})
        self.slyp.receive_word("ewordgam ")  # rotation of 'wordgame'
        self.assertDictEqual(
            self.slyp.word_length_map, {8: {"wordgame": {"wordgame", "ewordgam"}}}
        )

    def test_get_rotations(self):
        self.assertListEqual(self.slyp.get_rotations(), [])
        self.slyp.receive_word("wordgame")
        self.slyp.receive_word("ewordgam ")  # rotation of 'wordgame'
        self.slyp.receive_word("Slyp")
        self.slyp.receive_word("psly")
        self.slyp.receive_word("ypsl")
        self.slyp.receive_word("lyps")
        self.slyp.receive_word("lips")
        self.slyp.receive_word("cyan")
        self.assertCountEqual(
            [  # need to additionally sort since the list results are randomized
                sorted(result) for result in self.slyp.get_rotations()
            ],
            [
                ["ewordgam", "wordgame"],
                ["lyps", "psly", "slyp", "ypsl"],
                ["lips"],
                ["cyan"],
            ],
        )


if __name__ == "__main__":
    unittest.main(buffer=True)

