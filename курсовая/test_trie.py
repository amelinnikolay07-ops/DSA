"""Модульные тесты базовой структуры Trie. Запуск: python -m unittest -v"""

import unittest
from trie import Trie


class TrieTests(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.trie.insert("кот", 2)
        self.trie.insert("котик", 5)
        self.trie.insert("кошка", 3)
        self.trie.insert("дом", 1)

    def test_search_existing_word(self):
        self.assertTrue(self.trie.search("кот"))

    def test_search_missing_word(self):
        self.assertFalse(self.trie.search("пёс"))

    def test_prefix_is_not_necessarily_a_word(self):
        self.assertTrue(self.trie.starts_with("ко"))
        self.assertFalse(self.trie.search("ко"))

    def test_words_with_common_prefix(self):
        self.assertTrue(self.trie.search("кот"))
        self.assertTrue(self.trie.search("котик"))

    def test_frequency_increases_on_repeated_insertion(self):
        self.trie.insert("кот")
        self.assertEqual(self.trie.get_frequency("кот"), 3)

    def test_autocomplete_order(self):
        self.assertEqual(self.trie.autocomplete("ко"), [
            ("котик", 5), ("кошка", 3), ("кот", 2)
        ])

    def test_autocomplete_missing_prefix(self):
        self.assertEqual(self.trie.autocomplete("аб"), [])

    def test_search_path(self):
        visited, found = self.trie.search_path("котик")
        self.assertEqual(visited, ["к", "ко", "кот", "коти", "котик"])
        self.assertTrue(found)

    def test_empty_word_is_rejected(self):
        with self.assertRaises(ValueError):
            self.trie.insert("")


if __name__ == "__main__":
    unittest.main()
